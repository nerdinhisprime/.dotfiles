#!/bin/bash

setup_portals() {
  sudo pacman -S --noconfirm --needed xdg-desktop-portal xdg-desktop-portal-gtk xdg-desktop-portal-gnome gnome-keyring

  systemctl --user enable --now gnome-keyring-daemon.service
  systemctl --user restart xdg-desktop-portal xdg-desktop-portal-gtk xdg-desktop-portal-gnome

  local path=".config/xdg-desktop-portal"

  ln -snf "$HOME/.dotfiles/home/$path" "$HOME/$path"

  ## Check status portals
  # systemctl --user status xdg-desktop-portal
}

setup_portals
