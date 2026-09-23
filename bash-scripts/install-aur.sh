#!/bin/bash

install_aur() {
  sudo pacman -S --noconfirm --needed git

  local TMP_AUR="/tmp/yay-bin"
  rm -rf "$TMP_AUR"
  git clone https://aur.archlinux.org/yay-bin.git "$TMP_AUR"
  cd "$TMP_AUR" && makepkg -si --noconfirm
  cd $HOME
}

install_aur
