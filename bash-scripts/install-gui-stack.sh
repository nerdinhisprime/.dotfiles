#!/bin/bash

install_gui_stack() {
  shopt -s dotglob nullglob

  for config in "$HOME/.dotfiles/home/.config/"*; do
    ln -snf "$config" "$HOME/.config/"
  done

  shopt -u dotglob nullglob

  sudo pacman -S --noconfirm --needed niri foot waybar awww pcmanfm mako wlsunset brightnessctl openh264
}

install_gui_stack
