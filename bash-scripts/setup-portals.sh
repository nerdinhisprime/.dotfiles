#!/bin/bash

setup_portals() {
  systemctl --user enable --now gnome-keyring-daemon.service
  systemctl --user restart xdg-desktop-portal xdg-desktop-portal-gtk xdg-desktop-portal-gnome

  ## Check status portals
  # systemctl --user status xdg-desktop-portal
}

setup_portals
