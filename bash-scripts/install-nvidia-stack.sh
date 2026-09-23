#!/bin/bash

install_nvidia_stack() {
  sudo pacman -S --noconfirm --needed nvidia-dkms nvidia-utils lib32-nvidia-utils
}

install_gui_stack
