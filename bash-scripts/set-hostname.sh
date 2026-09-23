#!/bin/bash

set_hostname() {
  local new_hostname

  read -r -p "host name: " new_hostname

  if [[ -z "$new_hostname" ]]; then
    echo "\nError: host name cannot be empty.\n"
    return 1
  fi

  sudo hostnamectl set-hostname "$new_hostname"
}

set_hostname
