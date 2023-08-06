"""The client-object and its methods."""
from __future__ import annotations

from abc import ABC, abstractmethod
import logging
import time
from typing import Any

from hahomematic import config
import hahomematic.central_unit as hm_central
from hahomematic.const import (
    ATTR_ADDRESS,
    ATTR_CHANNELS,
    ATTR_ERROR,
    ATTR_HM_ADDRESS,
    ATTR_HM_NAME,
    ATTR_HM_PARAMSETS,
    ATTR_NAME,
    ATTR_RESULT,
    ATTR_VALUE,
    BACKEND_CCU,
    BACKEND_HOMEGEAR,
    BACKEND_PYDEVCCU,
    HM_VIRTUAL_REMOTES,
    PROXY_DE_INIT_FAILED,
    PROXY_DE_INIT_SKIPPED,
    PROXY_DE_INIT_SUCCESS,
    PROXY_INIT_FAILED,
    PROXY_INIT_SUCCESS,
    RELEVANT_PARAMSETS,
)
from hahomematic.device import HmDevice
from hahomematic.helpers import build_api_url, get_local_ip, parse_ccu_sys_var
from hahomematic.json_rpc_client import JsonRpcAioHttpClient
from hahomematic.xml_rpc_proxy import NoConnection, ProxyException, XmlRpcProxy

_LOGGER = logging.getLogger(__name__)


class Client(ABC):
    """
    Client object that initializes the XML-RPC proxy
    and provides access to other data via XML-RPC
    or JSON-RPC.
    """

    def __init__(self, client_config: ClientConfig):
        """
        Initialize the Client.
        """
        self._client_config: ClientConfig = client_config
        self._central: hm_central.CentralUnit = self._client_config.central
        self._version: str | None = self._client_config.version
        self.name: str = self._client_config.name
        # This is the actual interface_id used for init
        self.interface_id: str = f"{self._central.instance_name}-{self.name}"
        self._has_credentials = self._client_config.has_credentials
        self._init_url: str = self._client_config.init_url
        # for all device related interaction
        self.proxy: XmlRpcProxy = self._client_config.xml_rpc_proxy
        self.time_initialized: int = 0
        self._json_rpc_session: JsonRpcAioHttpClient = self._central.json_rpc_session

        self._central.clients[self.interface_id] = self
        if self._init_url not in self._central.clients_by_init_url:
            self._central.clients_by_init_url[self._init_url] = []
        self._central.clients_by_init_url[self._init_url].append(self)

    @property
    def version(self) -> str | None:
        """Return the version of the backend."""
        return self._version

    @property
    def model(self) -> str:
        """Return the model of the backend."""
        return ""

    @property
    def central(self) -> hm_central.CentralUnit:
        """Return the central of the backend."""
        return self._central

    async def proxy_init(self) -> int:
        """
        To receive events the proxy has to tell the CCU / Homegear
        where to send the events. For that we call the init-method.
        """
        try:
            _LOGGER.debug(
                "proxy_init: init('%s', '%s')", self._init_url, self.interface_id
            )
            await self.proxy.init(self._init_url, self.interface_id)
            _LOGGER.info("proxy_init: Proxy for %s initialized", self.name)
        except ProxyException:
            _LOGGER.exception(
                "proxy_init: Failed to initialize proxy for %s", self.name
            )
            self.time_initialized = 0
            return PROXY_INIT_FAILED
        self.time_initialized = int(time.time())
        return PROXY_INIT_SUCCESS

    async def proxy_de_init(self) -> int:
        """
        De-init to stop CCU from sending events for this remote.
        """
        if self._json_rpc_session.is_activated:
            await self._json_rpc_session.logout()
        if not self.time_initialized:
            _LOGGER.debug(
                "proxy_de_init: Skipping de-init for %s (not initialized)", self.name
            )
            return PROXY_DE_INIT_SKIPPED
        try:
            _LOGGER.debug("proxy_de_init: init('%s')", self._init_url)
            await self.proxy.init(self._init_url)
        except ProxyException:
            _LOGGER.exception(
                "proxy_de_init: Failed to de-initialize proxy for %s", self.name
            )
            return PROXY_DE_INIT_FAILED

        self.time_initialized = 0
        return PROXY_DE_INIT_SUCCESS

    async def proxy_re_init(self) -> int:
        """Reinit Proxy"""
        de_init_status = await self.proxy_de_init()
        if de_init_status is not PROXY_DE_INIT_FAILED:
            return await self.proxy_init()
        return PROXY_DE_INIT_FAILED

    def stop(self) -> None:
        """Stop depending services."""
        self.proxy.stop()

    @abstractmethod
    async def fetch_names(self) -> None:
        """Fetch names from backend."""
        ...

    async def is_connected(self) -> bool:
        """
        Perform actions required for connectivity check.
        Return connectivity state.
        """
        is_connected = await self._check_connection()
        if not is_connected:
            return False

        diff = int(time.time()) - self.time_initialized
        if diff < config.INIT_TIMEOUT:
            return True
        return False

    @abstractmethod
    async def _check_connection(self) -> bool:
        """Send ping to CCU to generate PONG event."""
        ...

    @abstractmethod
    async def set_system_variable(self, name: str, value: Any) -> None:
        """Set a system variable on CCU / Homegear."""
        ...

    @abstractmethod
    async def delete_system_variable(self, name: str) -> None:
        """Delete a system variable from CCU / Homegear."""
        ...

    @abstractmethod
    async def get_system_variable(self, name: str) -> str:
        """Get single system variable from CCU / Homegear."""
        ...

    @abstractmethod
    async def get_all_system_variables(self) -> dict[str, Any]:
        """Get all system variables from CCU / Homegear."""
        ...

    @abstractmethod
    def get_virtual_remote(self) -> HmDevice | None:
        """Get the virtual remote for the Client."""
        ...

    async def get_service_messages(self) -> Any:
        """Get service messages from CCU / Homegear."""
        try:
            return await self.proxy.getServiceMessages()
        except ProxyException:
            _LOGGER.exception("get_service_messages: ProxyException")
        return None

    # pylint: disable=invalid-name
    async def set_install_mode(
        self, on: bool = True, t: int = 60, mode: int = 1, address: str | None = None
    ) -> None:
        """Activate or deactivate installmode on CCU / Homegear."""
        try:
            args: list[Any] = [on]
            if on and t:
                args.append(t)
                if address:
                    args.append(address)
                else:
                    args.append(mode)

            await self.proxy.setInstallMode(*args)
        except ProxyException:
            _LOGGER.exception("set_install_mode: ProxyException")

    async def get_install_mode(self) -> Any:
        """Get remaining time in seconds install mode is active from CCU / Homegear."""
        try:
            return await self.proxy.getInstallMode()
        except ProxyException:
            _LOGGER.exception("get_install_mode: ProxyException")
        return 0

    # async def get_all_metadata(self, address: str):
    #     """Get all metadata of device."""
    #     try:
    #         return await self.proxy.getAllMetadata(address)
    #     except ProxyException:
    #         _LOGGER.exception("get_all_metadata: ProxyException")
    #
    # async def get_metadata(self, address: str, key: str):
    #     """Get metadata of device."""
    #     try:
    #         return await self.proxy.getMetadata(address, key)
    #     except ProxyException:
    #         _LOGGER.exception("get_metadata: ProxyException")
    #
    # async def set_metadata(self, address: str, key: str, value: Any):
    #     """Set metadata of device."""
    #     try:
    #         return await self.proxy.setMetadata(address, key, value)
    #     except ProxyException:
    #         _LOGGER.exception(".set_metadata: ProxyException")
    #
    # async def delete_metadata(self, address: str, key: str):
    #     """Delete metadata of device."""
    #     try:
    #         return await self.proxy.deleteMetadata(address, key)
    #     except ProxyException:
    #         _LOGGER.exception("delete_metadata: ProxyException")
    #
    # async def list_bidcos_interfaces(self):
    #     """Return all available BidCos Interfaces."""
    #     try:
    #         return await self.proxy.listBidcosInterfaces()
    #     except ProxyException:
    #         _LOGGER.exception("list_bidcos_interfaces: ProxyException")

    async def set_value(
        self, address: str, value_key: str, value: Any, rx_mode: str | None = None
    ) -> None:
        """Set single value on paramset VALUES."""
        try:
            if rx_mode:
                await self.proxy.setValue(address, value_key, value, rx_mode)
            else:
                await self.proxy.setValue(address, value_key, value)
        except ProxyException:
            _LOGGER.exception("set_value: ProxyException")

    async def put_paramset(
        self, address: str, paramset: str, value: Any, rx_mode: str | None = None
    ) -> None:
        """Set paramsets manually."""
        try:
            if rx_mode:
                await self.proxy.putParamset(address, paramset, value, rx_mode)
            else:
                await self.proxy.putParamset(address, paramset, value)

        except ProxyException:
            _LOGGER.exception("put_paramset: ProxyException")

    async def fetch_paramset(self, address: str, paramset: str) -> None:
        """
        Fetch a specific paramset and add it to the known ones.
        """
        _LOGGER.debug("Fetching paramset %s for %s", paramset, address)

        try:
            parameter_data = await self.proxy.getParamsetDescription(address, paramset)
            self._central.paramsets.add(
                interface_id=self.interface_id,
                address=address,
                paramset=paramset,
                paramset_description=parameter_data,
            )
        except ProxyException:
            _LOGGER.exception(
                "Unable to get paramset %s for address %s.", paramset, address
            )
        await self._central.paramsets.save()

    async def fetch_paramsets(
        self, device_description: dict[str, Any], update: bool = False
    ) -> None:
        """
        Fetch paramsets for provided device description.
        """
        address = device_description[ATTR_HM_ADDRESS]
        _LOGGER.debug("Fetching paramsets for %s", address)
        for paramset in RELEVANT_PARAMSETS:
            if paramset not in device_description[ATTR_HM_PARAMSETS]:
                continue
            try:
                paramset_description = await self.proxy.getParamsetDescription(
                    address, paramset
                )
                self._central.paramsets.add(
                    interface_id=self.interface_id,
                    address=address,
                    paramset=paramset,
                    paramset_description=paramset_description,
                )
            except ProxyException:
                _LOGGER.exception(
                    "Unable to get paramset %s for address %s.", paramset, address
                )

    async def fetch_all_paramsets(self, skip_existing: bool = False) -> None:
        """
        Fetch all paramsets for provided interface id.
        """
        for address, dd in self._central.raw_devices.get_interface(
            interface_id=self.interface_id
        ).items():
            if skip_existing and address in self._central.paramsets.get_by_interface(
                self.interface_id
            ):
                continue
            await self.fetch_paramsets(dd)
        await self._central.paramsets.save()

    async def update_paramsets(self, address: str) -> None:
        """
        Update paramsets for provided address.
        """
        if not self._central.raw_devices.get_interface(interface_id=self.interface_id):
            _LOGGER.warning(
                "Interface ID missing in central_unit.raw_devices.devices_raw_dict. Not updating paramsets for %s.",
                address,
            )
            return
        if not self._central.raw_devices.get_device(
            interface_id=self.interface_id, address=address
        ):
            _LOGGER.warning(
                "Channel missing in central_unit.raw_devices.devices_raw_dict[_interface_id]. Not updating paramsets for %s.",
                address,
            )
            return
        await self.fetch_paramsets(
            self._central.raw_devices.get_device(
                interface_id=self.interface_id, address=address
            ),
            update=True,
        )
        await self._central.paramsets.save()


class ClientCCU(Client):
    """Client implementation for CCU backend."""

    @property
    def model(self) -> str:
        """Return the model of the backend."""
        return BACKEND_CCU

    async def fetch_names(self) -> None:
        """
        Get all names via JSON-RPS and store in data.NAMES.
        """
        if not self._has_credentials:
            _LOGGER.warning(
                "fetch_names_json: No username set. Not fetching names via JSON-RPC."
            )
            return
        _LOGGER.debug("fetch_names_json: Fetching names via JSON-RPC.")
        try:
            response = await self._json_rpc_session.post(
                "Device.listAllDetail",
            )
            if response[ATTR_ERROR] is None and response[ATTR_RESULT]:
                _LOGGER.debug("fetch_names_json: Resolving devicenames")
                for device in response[ATTR_RESULT]:
                    self._central.names.add(device[ATTR_ADDRESS], device[ATTR_NAME])
                    for channel in device.get(ATTR_CHANNELS, []):
                        self._central.names.add(
                            channel[ATTR_ADDRESS], channel[ATTR_NAME]
                        )
        except Exception:
            _LOGGER.exception("fetch_names_json: General exception")

    async def _check_connection(self) -> bool:
        """Check if _proxy is still initialized."""
        try:
            success = await self.proxy.ping(self.interface_id)
            if success:
                self.time_initialized = int(time.time())
                return True
        except NoConnection:
            _LOGGER.exception("ping: NoConnection")
        except ProxyException:
            _LOGGER.exception("ping: ProxyException")
        self.time_initialized = 0
        return False

    async def set_system_variable(self, name: str, value: Any) -> None:
        """Set a system variable on CCU / Homegear."""
        if not self._has_credentials:
            _LOGGER.warning(
                "set_system_variable: You have to set username ans password to set a system variable via JSON-RPC"
            )
            return
        _LOGGER.debug("set_system_variable: Setting System variable via JSON-RPC")
        try:
            params = {
                ATTR_NAME: name,
                ATTR_VALUE: value,
            }
            if value is True or value is False:
                params[ATTR_VALUE] = int(value)
                response = await self._json_rpc_session.post("SysVar.setBool", params)
            else:
                response = await self._json_rpc_session.post("SysVar.setFloat", params)
            if response[ATTR_ERROR] is None and response[ATTR_RESULT]:
                res = response[ATTR_RESULT]
                _LOGGER.debug(
                    "set_system_variable: Result while setting variable: %s",
                    str(res),
                )
            else:
                if response[ATTR_ERROR]:
                    _LOGGER.debug(
                        "set_system_variable: Error while setting variable: %s",
                        str(response[ATTR_ERROR]),
                    )
        except Exception:
            _LOGGER.exception("set_system_variable: Exception")

    async def delete_system_variable(self, name: str) -> None:
        """Delete a system variable from CCU / Homegear."""
        if not self._has_credentials:
            _LOGGER.warning(
                "delete_system_variable: You have to set username ans password to delete a system variable via JSON-RPC"
            )
            return

        _LOGGER.debug("delete_system_variable: Getting System variable via JSON-RPC")
        try:
            params = {ATTR_NAME: name}
            response = await self._json_rpc_session.post(
                "SysVar.deleteSysVarByName",
                params,
            )
            if response[ATTR_ERROR] is None and response[ATTR_RESULT]:
                deleted = response[ATTR_RESULT]
                _LOGGER.info("delete_system_variable: Deleted: %s", str(deleted))
        except Exception:
            _LOGGER.exception("delete_system_variable: Exception")

    async def get_system_variable(self, name: str) -> Any:
        """Get single system variable from CCU / Homegear."""
        var = None
        if not self._has_credentials:
            _LOGGER.warning(
                "get_system_variable: You have to set username ans password to get a system variable via JSON-RPC"
            )
            return var

        _LOGGER.debug("get_system_variable: Getting System variable via JSON-RPC")
        try:
            params = {ATTR_NAME: name}
            response = await self._json_rpc_session.post(
                "SysVar.getValueByName",
                params,
            )
            if response[ATTR_ERROR] is None and response[ATTR_RESULT]:
                # This does not yet support strings
                try:
                    var = float(response[ATTR_RESULT])
                except Exception:
                    var = response[ATTR_RESULT] == "true"
        except Exception:
            _LOGGER.exception("get_system_variable: Exception")

        return var

    async def get_all_system_variables(self) -> dict[str, Any]:
        """Get all system variables from CCU / Homegear."""
        variables: dict[str, Any] = {}
        if not self._has_credentials:
            _LOGGER.warning(
                "get_all_system_variables: You have to set username ans password to get system variables via JSON-RPC"
            )
            return variables

        _LOGGER.debug(
            "get_all_system_variables: Getting all System variables via JSON-RPC"
        )
        try:
            response = await self._json_rpc_session.post(
                "SysVar.getAll",
            )
            if response[ATTR_ERROR] is None and response[ATTR_RESULT]:
                for var in response[ATTR_RESULT]:
                    key, value = parse_ccu_sys_var(var)
                    variables[key] = value
        except Exception:
            _LOGGER.exception("get_all_system_variables: Exception")

        return variables

    def get_virtual_remote(self) -> HmDevice | None:
        """Get the virtual remote for the Client."""
        for virtual_address in HM_VIRTUAL_REMOTES:
            virtual_remote = self._central.hm_devices.get(virtual_address)
            if virtual_remote and virtual_remote.interface_id == self.interface_id:
                return virtual_remote
        return None


class ClientHomegear(Client):
    """Client implementation for Homegear backend."""

    @property
    def model(self) -> str:
        """Return the model of the backend."""
        if self.version:
            return (
                BACKEND_PYDEVCCU
                if BACKEND_PYDEVCCU.lower() in self.version
                else BACKEND_HOMEGEAR
            )
        return BACKEND_CCU

    async def fetch_names(self) -> None:
        """
        Get all names from metadata (Homegear).
        """
        _LOGGER.debug("fetch_names_metadata: Fetching names via Metadata.")
        for address in self._central.raw_devices.get_interface(
            interface_id=self.interface_id
        ):
            try:
                self._central.names.add(
                    address,
                    await self.proxy.getMetadata(address, ATTR_HM_NAME),
                )
            except ProxyException:
                _LOGGER.exception("Failed to fetch name for device %s.", address)

    async def _check_connection(self) -> bool:
        """Check if proxy is still initialized."""
        try:
            if await self.proxy.clientServerInitialized(self.interface_id):
                self.time_initialized = int(time.time())
                return True
        except NoConnection:
            _LOGGER.exception("ping: NoConnection")
        except ProxyException:
            _LOGGER.exception("homegear_check_init: ProxyException")
        _LOGGER.warning(
            "homegear_check_init: Setting initialized to 0 for %s", self.interface_id
        )
        self.time_initialized = 0
        return False

    async def set_system_variable(self, name: str, value: Any) -> None:
        """Set a system variable on CCU / Homegear."""
        try:
            await self.proxy.setSystemVariable(name, value)
        except ProxyException:
            _LOGGER.exception("set_system_variable: ProxyException")

    async def delete_system_variable(self, name: str) -> None:
        """Delete a system variable from CCU / Homegear."""
        try:
            await self.proxy.deleteSystemVariable(name)
        except ProxyException:
            _LOGGER.exception("delete_system_variable: ProxyException")

    async def get_system_variable(self, name: str) -> Any:
        """Get single system variable from CCU / Homegear."""
        try:
            return await self.proxy.getSystemVariable(name)
        except ProxyException:
            _LOGGER.exception("get_system_variable: ProxyException")

    async def get_all_system_variables(self) -> Any:
        """Get all system variables from CCU / Homegear."""
        try:
            return await self.proxy.getAllSystemVariables()
        except ProxyException:
            _LOGGER.exception("get_all_system_variables: ProxyException")
        return None

    def get_virtual_remote(self) -> HmDevice | None:
        """Get the virtual remote for the Client."""
        return None


class ClientConfig:
    """Config for a Client."""

    def __init__(
        self,
        central: hm_central.CentralUnit,
        name: str,
        port: int,
        path: str | None = None,
    ):
        self.central = central
        self.name = name
        self._central_config = self.central.central_config
        self._callback_host: str = (
            self._central_config.callback_host
            if self._central_config.callback_host
            else get_local_ip(host=self._central_config.host, port=port)
        )
        self._callback_port: int = (
            self._central_config.callback_port
            if self._central_config.callback_port
            else self.central.local_port
        )
        self.init_url: str = f"http://{self._callback_host}:{self._callback_port}"
        self.api_url = build_api_url(
            host=self._central_config.host,
            port=port,
            path=path,
            username=self._central_config.username,
            password=self._central_config.password,
            tls=self._central_config.tls,
        )
        self.has_credentials: bool = (
            self._central_config.username is not None
            and self._central_config.password is not None
        )
        self.version: str | None = None
        self.xml_rpc_proxy: XmlRpcProxy = XmlRpcProxy(
            self.central.loop,
            self.api_url,
            tls=self._central_config.tls,
            verify_tls=self._central_config.verify_tls,
        )

    async def get_client(self) -> Client:
        """Identify the used client."""
        try:
            self.version = await self.xml_rpc_proxy.getVersion()
        except ProxyException as err:
            raise ProxyException(
                f"Failed to get backend version. Not creating client: {self.api_url}"
            ) from err
        if self.version:
            if "Homegear" in self.version or "pydevccu" in self.version:
                return ClientHomegear(self)
        return ClientCCU(self)
