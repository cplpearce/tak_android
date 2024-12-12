import logging
import os
import signal
import time

from abc import ABC, abstractmethod
from enum import Enum

from src.constants import DEVICE, ENV


class DeviceType(Enum):
    EMULATOR = "emulator"


class Device(ABC):
    FORM_USER = "user"
    FORM_CITY = "city"
    FORM_REGION = "region"
    FORM_COUNTRY = "country"
    FORM_APP_VERSION = "app_version"
    FORM_APPIUM = "appium"
    FORM_APPIUM_ADDITIONAL_ARGS = "appium_additional_args"
    FORM_WEB_LOG = "web_log"
    FORM_WEB_VNC = "web_vnc"
    FORM_SCREEN_RESOLUTION = "screen_resolution"
    FORM_DEVICE_TYPE = "device_type"
    FORM_EMU_DEVICE = "emu_device"
    FORM_EMU_ANDROID_VERSION = "emu_android_version"
    FORM_EMU_NO_SKIN = "emu_no_skin"
    FORM_EMU_DATA_PARTITION = "emu_data_partition"
    FORM_EMU_ADDITIONAL_ARGS = "emu_additional_args"

    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.device_type = None
        self.interval_waiting = int(os.getenv(ENV.DEVICE_INTERVAL_WAITING, 2))
        self.user_behavior_analytics = False
        self.form_field = {
            Device.FORM_USER: "entry.108751316",
            Device.FORM_CITY: "entry.2083022547",
            Device.FORM_REGION: "entry.1083141079",
            Device.FORM_COUNTRY: "entry.1946159560",
            Device.FORM_APP_VERSION: "entry.818050927",
            Device.FORM_WEB_LOG: "entry.1225589007",
            Device.FORM_WEB_VNC: "entry.2055392048",
            Device.FORM_SCREEN_RESOLUTION: "entry.709976626",
            Device.FORM_DEVICE_TYPE: "entry.207096546",
            Device.FORM_EMU_DEVICE: "entry.1960740382",
            Device.FORM_EMU_ANDROID_VERSION: "entry.671872491",
            Device.FORM_EMU_NO_SKIN: "entry.403556951",
            Device.FORM_EMU_DATA_PARTITION: "entry.1052258875",
            Device.FORM_EMU_ADDITIONAL_ARGS: "entry.57529972",
        }
        self.form_data = {}
        signal.signal(signal.SIGTERM, self.tear_down)

    def set_status(self, current_status) -> None:
        bashrc_file = f"{os.getenv(ENV.WORK_PATH)}/device_status"
        with open(bashrc_file, "w+") as bf:
            bf.write(current_status)
        # It won't work using docker ex_prepare_analytics_payloadec
        # os.environ[constants.ENV_DEVICE_STATUS] = current_status

    def create(self) -> None:
        self.set_status(DEVICE.STATUS_CREATING)

    def start(self) -> None:
        self.set_status(DEVICE.STATUS_STARTING)

    def wait_until_ready(self) -> None:
        self.set_status(DEVICE.STATUS_BOOTING)

    def reconfigure(self) -> None:
        self.set_status(DEVICE.STATUS_RECONFIGURING)

    def keep_alive(self) -> None:
        self.set_status(DEVICE.STATUS_READY)
        self.logger.warning(
            f"{self.device_type} process will be kept alive to be able to get sigterm signal..."
        )
        while True:
            time.sleep(2)

    @abstractmethod
    def tear_down(self, *args) -> None:
        pass
