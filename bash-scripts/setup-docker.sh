#!/bin/bash

setup_docker() {
  sudo pacman -S docker docker-compose

  sudo systemctl enable --now docker.service
  sudo usermod -aG docker $USER
}

setup_docker
