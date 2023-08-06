__version__ = "0.1.0"

import ctypes
import logging
import subprocess
import sys
import time
import warnings
from contextlib import contextmanager
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import List, Literal, Optional, get_args

import pywintypes
import win32api
import win32con
import win32service
import win32serviceutil
import winerror


@dataclass(frozen=True)
class ServiceType:
    """Represents the dwServiceType field of the SERVICE_STATUS or QUERY_SERVICE_CONFIGA
    structure.

    See these links for more info:

    https://docs.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_status#members
    https://docs.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-query_service_configa#members
    """

    ltype = Literal[
        0x00000001,  # SERVICE_KERNEL_DRIVER
        0x00000002,  # SERVICE_FILE_SYSTEM_DRIVER
        0x00000010,  # SERVICE_WIN32_OWN_PROCESS
        0x00000020,  # SERVICE_WIN32_SHARE_PROCESS
        0x00000030,  # SERVICE_WIN32
        0x00000050,  # SERVICE_USER_OWN_PROCESS
        0x00000060,  # SERVICE_USER_SHARE_PROCESS
        0x000000D0,  # USER_OWN_PROCESS (instance)
        0x000000E0,  # USER_SHARE_PROCESS (instance)
        0x00000100,  # SERVICE_INTERACTIVE_PROCESS
        0x00000110,  # WIN32_OWN_PROCESS (interactive)
        0x00000130,  # WIN32 (interactive)
        0x000000F0,  # ERROR
    ]

    value: ltype

    SERVICE_USER_OWN_PROCESS = 0x00000050
    SERVICE_USER_SHARE_PROCESS = 0x00000060
    USER_SHARE_PROCESS_INSTANCE = 0x000000E0
    USER_OWN_PROCESS_INSTANCE = 0x000000D0
    WIN32_INTERACTIVE = (
        win32service.SERVICE_WIN32 | win32service.SERVICE_INTERACTIVE_PROCESS
    )
    WIN32_OWN_PROCESS_INTERACTIVE = (
        win32service.SERVICE_WIN32_OWN_PROCESS
        | win32service.SERVICE_INTERACTIVE_PROCESS
    )
    ERROR = 0x0000000F0

    value_to_ms_name = {
        win32service.SERVICE_FILE_SYSTEM_DRIVER: "SERVICE_FILE_SYSTEM_DRIVER",
        win32service.SERVICE_KERNEL_DRIVER: "SERVICE_KERNEL_DRIVER",
        win32service.SERVICE_WIN32: "SERVICE_WIN32",
        win32service.SERVICE_WIN32_OWN_PROCESS: "SERVICE_WIN32_OWN_PROCESS",
        win32service.SERVICE_WIN32_SHARE_PROCESS: "SERVICE_WIN32_SHARE_PROCESS",
        win32service.SERVICE_INTERACTIVE_PROCESS: "SERVICE_INTERACTIVE_PROCESS",
        SERVICE_USER_OWN_PROCESS: "SERVICE_USER_OWN_PROCESS",
        SERVICE_USER_SHARE_PROCESS: "SERVICE_USER_SHARE_PROCESS",
        USER_SHARE_PROCESS_INSTANCE: "USER_SHARE_PROCESS INSTANCE",
        USER_OWN_PROCESS_INSTANCE: "USER_OWN_PROCESS INSTANCE",
        WIN32_INTERACTIVE: "WIN32 (interactive)",
        WIN32_OWN_PROCESS_INTERACTIVE: "WIN32_OWN_PROCESS (interactive)",
        ERROR: "ERROR",
    }

    def __post_init__(self):
        if self.value not in self.value_to_ms_name:
            # used for tracking down unknown values
            raise ValueError(f"Unknown service type: {self.value}")

        # sanity check our value Literal values for development purposes
        field_types = {field.name: field.type for field in fields(self.__class__)}
        l = sorted(get_args(field_types["value"]))
        sorted1 = sorted(self.value_to_ms_name.keys())
        if not l == sorted1:
            warnings.warn(
                "Inform developers of this warning:  ServiceType.value type is out of "
                "date.  Please update it.\n"
                f"{l}\n"
                f"{sorted1}\n"
            )

    @property
    def is_file_system_driver(self):
        return self.value == win32service.SERVICE_FILE_SYSTEM_DRIVER

    @property
    def is_kernel_driver(self):
        return self.value == win32service.SERVICE_KERNEL_DRIVER

    @property
    def is_win32_own_process(self):
        return self.value == win32service.SERVICE_WIN32_OWN_PROCESS

    @property
    def is_win32_share_process(self):
        return self.value == win32service.SERVICE_WIN32_SHARE_PROCESS

    @property
    def is_interactive_process(self):
        return self.value == win32service.SERVICE_INTERACTIVE_PROCESS

    @property
    def is_user_own_process(self):
        return self.value == self.SERVICE_USER_OWN_PROCESS

    @property
    def is_user_share_process(self):
        return self.value == self.SERVICE_USER_SHARE_PROCESS

    @property
    def type(self):
        return self.value_to_ms_name.get(self.value, "UNKNOWN")

    def __repr__(self):
        return f"<ServiceType: {self.value} ({self.type})>"


@dataclass(frozen=True)
class ServiceStartType:
    value: Literal[2, 0, 3, 4, 1]
    service_name: str

    value_to_ms_name = {
        win32service.SERVICE_AUTO_START: "SERVICE_AUTO_START",
        win32service.SERVICE_BOOT_START: "SERVICE_BOOT_START",
        win32service.SERVICE_DEMAND_START: "SERVICE_DEMAND_START",
        win32service.SERVICE_DISABLED: "SERVICE_DISABLED",
        win32service.SERVICE_SYSTEM_START: "SERVICE_SYSTEM_START",
    }

    def __repr__(self):
        return f"<ServiceStartType: {self.value} ({self.type})>"

    @property
    def auto(self):
        return self.value == win32service.SERVICE_AUTO_START

    @property
    def boot(self):
        return self.value == win32service.SERVICE_BOOT_START

    @property
    def is_demand(self):
        return self.value == win32service.SERVICE_DEMAND_START

    @property
    def disabled(self):
        return self.value == win32service.SERVICE_DISABLED

    @property
    def system(self):
        return self.value == win32service.SERVICE_SYSTEM_START

    @property
    def type(self):
        return self.value_to_ms_name.get(self.value, "UNKNOWN")

    def set_auto_start(self, wait_for_seconds: int = 10):
        self.set_start_type(win32service.SERVICE_AUTO_START, wait_for_seconds)

    def set_boot_start(self, wait_for_seconds: int = 10):
        self.set_start_type(win32service.SERVICE_BOOT_START, wait_for_seconds)

    def set_demand_start(self, wait_for_seconds: int = 10):
        self.set_start_type(win32service.SERVICE_DEMAND_START, wait_for_seconds)

    def set_disabled(self, wait_for_seconds: int = 10):
        self.set_start_type(win32service.SERVICE_DISABLED, wait_for_seconds)

    def set_system_start(self, wait_for_seconds: int = 10):
        self.set_start_type(win32service.SERVICE_SYSTEM_START, wait_for_seconds)

    def set_start_type(
        self,
        start_type: Literal[2, 0, 3, 4, 1],
        wait_for_seconds: int = 10,
    ):
        win32serviceutil.ChangeServiceConfig(
            None, self.service_name, startType=start_type
        )

        wait_for_service_config_status(self.service_name, start_type, wait_for_seconds)


@dataclass(frozen=True)
class ServiceState:
    value: Literal[5, 6, 7, 4, 2, 3, 1]
    service_name: str

    value_to_ms_name = {
        win32service.SERVICE_CONTINUE_PENDING: "SERVICE_CONTINUE_PENDING",
        win32service.SERVICE_PAUSE_PENDING: "SERVICE_PAUSE_PENDING",
        win32service.SERVICE_PAUSED: "SERVICE_PAUSED",
        win32service.SERVICE_RUNNING: "SERVICE_RUNNING",
        win32service.SERVICE_START_PENDING: "SERVICE_START_PENDING",
        win32service.SERVICE_STOP_PENDING: "SERVICE_STOP_PENDING",
        win32service.SERVICE_STOPPED: "SERVICE_STOPPED",
    }

    @property
    def continue_pending(self):
        return self.value == win32service.SERVICE_CONTINUE_PENDING

    @property
    def pause_pending(self):
        return self.value == win32service.SERVICE_PAUSE_PENDING

    @property
    def paused(self):
        return self.value == win32service.SERVICE_PAUSED

    @property
    def running(self):
        return self.value == win32service.SERVICE_RUNNING

    @property
    def start_pending(self):
        return self.value == win32service.SERVICE_START_PENDING

    @property
    def stop_pending(self):
        return self.value == win32service.SERVICE_STOP_PENDING

    @property
    def stopped(self):
        return self.value == win32service.SERVICE_STOPPED

    @property
    def type(self):
        return self.value_to_ms_name.get(self.value, "UNKNOWN")

    def start(self, wait_for_seconds: int = 10):
        win32serviceutil.StartService(self.service_name)
        win32serviceutil.WaitForServiceStatus(
            self.service_name, win32service.SERVICE_RUNNING, wait_for_seconds
        )

    def stop(self, wait_for_seconds: int = 10):
        win32serviceutil.StopService(self.service_name)
        win32serviceutil.WaitForServiceStatus(
            self.service_name, win32service.SERVICE_STOPPED, wait_for_seconds
        )

    def __repr__(self):
        return f"<ServiceState: {self.value} ({self.type})>"


@dataclass(frozen=True)
class ServiceControls:
    value: Literal[16, 8, 2, 256, 4, 1, 32, 64, 128, 0x00000200, 0x00000400, 0x00000800]

    ACCEPT_TIMECHANGE = 0x00000200
    ACCEPT_TRIGGEREVENT = 0x00000400
    ACCEPT_USERMOREREBOOT = 0x00000800

    value_to_ms_name = {
        ACCEPT_TIMECHANGE: "ACCEPT_TIMECHANGE",
        ACCEPT_TRIGGEREVENT: "ACCEPT_TRIGGEREVENT",
        ACCEPT_USERMOREREBOOT: "ACCEPT_USERMOREREBOOT",
        win32service.SERVICE_ACCEPT_NETBINDCHANGE: "ACCEPT_NETBINDCHANGE",
        win32service.SERVICE_ACCEPT_PARAMCHANGE: "ACCEPT_PARAMCHANGE",
        win32service.SERVICE_ACCEPT_PAUSE_CONTINUE: "ACCEPT_PAUSE_CONTINUE",
        win32service.SERVICE_ACCEPT_PRESHUTDOWN: "ACCEPT_PRESHUTDOWN",
        win32service.SERVICE_ACCEPT_SHUTDOWN: "ACCEPT_SHUTDOWN",
        win32service.SERVICE_ACCEPT_STOP: "ACCEPT_STOP",
        win32service.SERVICE_ACCEPT_HARDWAREPROFILECHANGE: "ACCEPT_HARDWAREPROFILECHANGE",
        win32service.SERVICE_ACCEPT_POWEREVENT: "ACCEPT_POWEREVENT",
        win32service.SERVICE_ACCEPT_SESSIONCHANGE: "ACCEPT_SESSIONCHANGE",
    }

    @property
    def accepts_net_bind_change(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_NETBINDCHANGE)

    @property
    def accepts_param_change(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_PARAMCHANGE)

    @property
    def accepts_pause_continue(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_PAUSE_CONTINUE)

    @property
    def accepts_pre_shutdown(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_PRESHUTDOWN)

    @property
    def accepts_shutdown(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_SHUTDOWN)

    @property
    def accepts_stop(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_STOP)

    @property
    def accepts_hardware_profile_change(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_HARDWAREPROFILECHANGE)

    @property
    def accepts_power_event(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_POWEREVENT)

    @property
    def accepts_session_change(self):
        return bool(self.value & win32service.SERVICE_ACCEPT_SESSIONCHANGE)

    @property
    def accepts_time_change(self):
        return bool(self.value & self.ACCEPT_TIMECHANGE)

    @property
    def accepts_trigger_event(self):
        return bool(self.value & self.ACCEPT_TRIGGEREVENT)

    @property
    def accepts_user_more_reboot(self):
        return bool(self.value & self.ACCEPT_USERMOREREBOOT)

    @property
    def type(self):
        return self.value_to_ms_name.get(self.value, "UNKNOWN")

    def __repr__(self):
        return f"<ServiceControls {self.value} ({self.type})>"


@dataclass(frozen=True)
class ServiceStatus:
    service_type: ServiceType
    state: ServiceState
    controls_accepted: ServiceControls
    exit_code: int
    service_error_code: int
    check_point: int
    wait_hint: int

    @classmethod
    def create(cls, service_handle: int, service_name: str) -> "ServiceStatus":
        state = win32service.QueryServiceStatus(service_handle)
        service_type = ServiceType(state[0])
        service_state = ServiceState(state[1], service_name)
        controls_accepted = ServiceControls(state[2])
        return cls(
            service_type,
            service_state,
            controls_accepted,
            state[3],
            state[4],
            state[5],
            state[6],
        )


@dataclass(frozen=True)
class ServiceConfig:
    service_type: ServiceType
    start_type: ServiceStartType
    error_control: int
    binary_path_name: Path
    load_order_group: str
    tag_id: int
    dependencies: str
    service_start_name: str
    display_name: str

    @classmethod
    def create(cls, service_handle: int, service_name: str) -> "ServiceConfig":
        config = win32service.QueryServiceConfig(service_handle)
        service_type = ServiceType(config[0])
        start_type = ServiceStartType(config[1], service_name)
        path = Path(config[3])
        return cls(
            service_type=service_type,
            start_type=start_type,
            error_control=config[2],
            binary_path_name=path,
            load_order_group=config[4],
            tag_id=config[5],
            dependencies=config[6],
            service_start_name=config[7],
            display_name=config[8],
        )


@dataclass(frozen=True)
class ServiceControlManager:
    service_name: str

    _wait_timeout: int = field(repr=False, default=5)

    def __post_init__(self):
        # early raise if we don't have correct permissions
        logging.debug("Ensuring we have correct permissions for %s", self.service_name)
        with _get_svc_handle(self.service_name) as _:
            pass
        logging.debug("We have correct permissions for %s", self.service_name)

    def start(self) -> None:
        win32serviceutil.StartService(self.service_name)
        logging.debug("waiting for service %s to start", self.service_name)
        win32serviceutil.WaitForServiceStatus(
            self.service_name, win32service.SERVICE_RUNNING, self._wait_timeout
        )

    @property
    def status(self) -> ServiceStatus:
        with _get_svc_handle(self.service_name) as handle:
            return ServiceStatus.create(handle, self.service_name)

    @property
    def config(self) -> ServiceConfig:
        with _get_svc_handle(self.service_name) as handle:
            return ServiceConfig.create(handle, self.service_name)


@contextmanager
def stopped_service(
    service_name: str,
    ignore_stopped: bool = True,
    wait_for: int = 10,
    also_disable: bool = True,
) -> None:
    """
    Context manager to stop a service and then start it again.

    :param service_name: The name of the service to stop and start
    :param ignore_stopped: If True, don't raise if the service is already stopped. Default: True.
    :param wait_for: How long to wait for each of these actions: stop, disable, enable,
        start. Defaults to 10 seconds.
    :param also_disable: If True, disable the service after stopping it. Default: True.
    """
    service = ServiceControlManager(service_name)

    # stop the service
    previous_state = service.status.state
    logging.debug("Current service state: %s", previous_state)

    try:
        logging.debug("Stopping service %s", service_name)
        service.status.state.stop(wait_for_seconds=wait_for)
    except pywintypes.error as e:
        if e.winerror == winerror.ERROR_SERVICE_NOT_ACTIVE and ignore_stopped:
            # service is already stopped and we don't care
            logging.debug("Service %s is already stopped, ignoring.", service_name)
            pass
        else:
            # service is already stopped or some other error
            raise

    # disable the service
    previous_start_type = service.config.start_type
    logging.debug("Current service start type: %s", previous_start_type)

    if also_disable:
        logging.debug("Disabling service %s", service_name)
        service.config.start_type.set_disabled(wait_for_seconds=wait_for)

    # yield the service
    yield service

    # enable the service
    if also_disable and not previous_start_type.disabled:
        logging.debug(
            "Restoring start type to %s for service %s",
            previous_start_type,
            service_name,
        )
        service.config.start_type.set_start_type(
            previous_start_type.value, wait_for_seconds=wait_for
        )

    # start the service
    if any(
        [
            previous_state.running,
            previous_state.start_pending,
            previous_state.continue_pending,
        ]
    ):
        logging.debug("Restarting service %s", service_name)
        service.status.state.start(wait_for_seconds=wait_for)
    else:
        logging.debug(
            "Service %s previously had a state of %s, not starting.",
            service_name,
            previous_state,
        )


def wait_for_service_config_status(
    service_name: str, status: int, wait_seconds: int
) -> None:
    """
    Waits for a service to reach a certain status.

    Basically a straight rip-off of win32serviceutil.WaitForServiceStatus except using
    QueryServiceConfig instead of QueryServiceStatus.

    :param service_name: Name of the service to wait for.
    :param status: Status to wait for.
    :return: None
    """
    for i in range(wait_seconds * 4):
        with _get_svc_handle(service_name) as handle:
            now_status = win32service.QueryServiceConfig(handle)[1]
        if now_status == status:
            break
        win32api.Sleep(250)
    else:
        raise pywintypes.error(
            winerror.ERROR_SERVICE_REQUEST_TIMEOUT,
            "QueryServiceConfig",
            win32api.FormatMessage(winerror.ERROR_SERVICE_REQUEST_TIMEOUT)[:-2],
        )


@contextmanager
def _get_svc_handle(service_name: str) -> None:
    # some various combinations of permissions that I've found work to get a handle
    permission_combos = (
        (win32service.SC_MANAGER_ALL_ACCESS, win32service.SERVICE_ALL_ACCESS),
        (win32service.SC_MANAGER_CONNECT, win32service.SERVICE_CHANGE_CONFIG),
        (win32con.GENERIC_READ, win32service.SERVICE_ALL_ACCESS),
    )
    hs = None
    svc_ctrl_manager = None

    try:
        for idx, values in enumerate(permission_combos):
            sc_perm, svc_perm = values
            logging.debug("attempting to get service handle for %s", service_name)
            svc_ctrl_manager = win32service.OpenSCManager(None, None, sc_perm)
            logging.debug("opening service %s", service_name)

            try:
                hs = win32service.OpenService(svc_ctrl_manager, service_name, svc_perm)

            except pywintypes.error as e:
                if idx == len(permission_combos) - 1:
                    raise
                if e.winerror == winerror.ERROR_ACCESS_DENIED:
                    logging.debug("access denied, trying another permission combo")
                    continue

            if hs:
                logging.debug("got service handle for %s", service_name)

                yield hs
                break
    finally:
        if hs:
            logging.debug("closing service %s", service_name)
            win32service.CloseServiceHandle(hs)
        if svc_ctrl_manager:
            logging.debug("closing service manager")
            win32service.CloseServiceHandle(svc_ctrl_manager)
