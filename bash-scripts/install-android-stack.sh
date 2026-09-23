#!/bin/bash

install_android_stack() {
  sudo pacman -S --noconfirm --needed gvfs gvfs-mtp libmtp android-udev scrcpy
}

install_android_stack
