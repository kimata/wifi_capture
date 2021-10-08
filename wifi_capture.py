#!/usr/bin/env zsh
# WiFi のパケットキャプチャを行うスクリプトです．

set -eu

CH=${1:-1}
FILE=${2:-/tmp/wifi.cap}

sudo ifconfig wlan1 down
sudo iwconfig wlan1 mode monitor
sudo ifconfig wlan1 up
sudo iwconfig wlan1 channel $CH
sudo tshark -I -i wlan1 -w $FILE

