#!/bin/bash

setup_bluetooth() {
  sudo systemctl enable --now bluetooth.service
}

setup_bluetooth
