#!/bin/bash

install_packages() {
  sudo pacman -Syu
  sudo pacman -S --noconfirm --needed "$@"
}

install_packages "$@"
