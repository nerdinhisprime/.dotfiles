#!/bin/bash

install_cli_stack() {
    shopt -s dotglob nullglob

    for file in "$HOME/.dotfiles/home/".*; do
    local name="$(basename "$file")"
    if [[ "$name" != "." && "$name" != ".." && "$name" != ".config" && "$name" != ".local" ]]; then
      ln -snf "$file" "$HOME/$name"
    fi
    done

    shopt -u dotglob nullglob

    sudo pacman -S --noconfirm --needed openssh curl git ffmpeg
}

install_cli_stack
