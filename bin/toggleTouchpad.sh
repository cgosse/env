#!/bin/bash

device=`xinput list | grep -i touchpad | egrep -o "id=[0-9]*" | cut -d "=" -f2`
echo "found device $device for the touchpad"
state=`xinput list-props "$device" | grep "Device Enabled" | grep -o "[01]$"`

if [ $state == '1' ];then
  xinput --disable $device
else
  xinput --enable $device
fi