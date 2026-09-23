#!/bin/bash

setup_bluetooth() {
  sudo pacman -S --noconfirm bluez bluez-utils bluez-obex bluetui
  yay -S --noconfirm bluetuith-bin

  sudo systemctl enable --now bluetooth.service
  systemctl --user enable --now obex
}

setup_bluetooth
