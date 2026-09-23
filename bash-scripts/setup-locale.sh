#!/bin/bash

write_file() {
  printf "%b\n" "$2" | sudo tee "$1" > /dev/null
}

setup_locale() {
  write_file "/etc/locale.gen" "ru_RU.UTF-8 UTF-8\nen_US.UTF-8 UTF-8"
  write_file "/etc/locale.conf" "LANG=en_US.UTF-8"

  sudo locale-gen
}

setup_locale
