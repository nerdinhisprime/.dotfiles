#!/bin/bash

activate-custom-scripts() {
  chmod +x ~/.local/bin/* 2>/dev/null || true
  sudo usermod -aG network $USER
}

activate-custom-scripts
