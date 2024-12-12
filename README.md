# TAK ANDROID via Docker

<p align="center">
  <img id="header" src="./images/logo_docker-android.png" />
</p>

Docker-Android is a docker image built to be used for everything related to Android. It can be used for Application development and testing (native, web and hybrid-app).

## List of Devices

| Type   | Device Name            |
| ------ | ---------------------- |
| Phone  | Samsung Galaxy S10     |
| Phone  | Samsung Galaxy S9      |
| Phone  | Samsung Galaxy S8      |
| Phone  | Samsung Galaxy S7 Edge |
| Phone  | Samsung Galaxy S7      |
| Phone  | Samsung Galaxy S6      |
| Phone  | Nexus 4                |
| Phone  | Nexus 5                |
| Phone  | Nexus One              |
| Phone  | Nexus S                |
| Tablet | Nexus 7                |

## Requirements

1. Docker is installed on your system.

## Quick Start

1. If you use **_Ubuntu OS_** on your host machine, you can skip this step. For **_OSX_** and **_Windows OS_** user, you need to use Virtual Machine that support Virtualization with Ubuntu OS because the image can be run under **_Ubuntu OS only_**.

2. Your machine should support virtualization. To check if the virtualization is enabled is:

   ```bash
   sudo apt install cpu-checker
   kvm-ok
   ```

3. Run Docker-Android container

   ```bash
   docker run -d -p 6080:6080 -e EMULATOR_DEVICE="Samsung Galaxy S10" -e WEB_VNC=true --device /dev/kvm --name android-container mighthire/tak-android:emulator_11.0
   ```

4. Open <http://localhost:6080> to see inside running container.

5. To check the status of the emulator

   ```bash
   docker exec -it android-container cat device_status
   ```

## Persisting data

The default behaviour is to destroy the emulated device on container restart. To persist data, you need to mount a volume at `/home/androidusr`: `docker run -v data:/home/androidusr`

`command = /bin/bash -c 'chown -v root:kvm /dev/kvm && chmod 660 /dev/kvm'` sets `/dev/kvm` to `kvm` usergroup rather than the default `root` usergroup on WSL2 startup.

`nestedVirtualization` flag is only available to Windows 11.

## Custom-Configurations

This [document](./documentations/CUSTOM_CONFIGURATIONS.md) contains information about configurations that can be used to enable some features, e.g. log-sharing, etc.

## Emulator Skins

The Emulator skins are taken from [Android Studio IDE](https://developer.android.com/studio) and [Samsung Developer Website](https://developer.samsung.com/)

## Forked From <https://github.dev/budtmo/docker-android/>

- Removed a bunch of spyware
- Removed Genymotion eugh
