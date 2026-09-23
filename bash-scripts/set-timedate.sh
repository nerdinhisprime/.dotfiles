#!/bin/bash

set_timedate() {
  sudo timedatectl set-timezone Asia/Yekaterinburg
  sudo timedatectl set-ntp true
}

set_timedate
