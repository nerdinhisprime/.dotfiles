#!/bin/bash

setup_pipewire() {
  sudo pacman -S --noconfirm --needed pipewire pipewire-pulse pipewire-alsa wireplumber pulsemixer

  systemctl --user enable --now pipewire.service pipewire-pulse.service wireplumber.service
}

setup_pipewire
