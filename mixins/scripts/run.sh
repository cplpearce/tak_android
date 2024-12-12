#!/bin/bash

function shuwdown(){
  echo "SIGTERM is received! Clean-up will be executed if needed!"
  process_id=$(pgrep -f "start device")
  kill ${process_id}
  sleep 10
}

trap shuwdown SIGTERM

SUPERVISORD_CONFIG_PATH="${APP_PATH}/mixins/configs/process"
if [[ ${EMULATOR_HEADLESS} == true ]]; then
  /usr/bin/supervisord --configuration ${SUPERVISORD_CONFIG_PATH}/supervisord-port.conf & \
  /usr/bin/supervisord --configuration ${SUPERVISORD_CONFIG_PATH}/supervisord-base.conf & \
  wait
else
  /usr/bin/supervisord --configuration ${SUPERVISORD_CONFIG_PATH}/supervisord-screen.conf & \
  /usr/bin/supervisord --configuration ${SUPERVISORD_CONFIG_PATH}/supervisord-port.conf & \
  /usr/bin/supervisord --configuration ${SUPERVISORD_CONFIG_PATH}/supervisord-base.conf & \
  wait
fi
