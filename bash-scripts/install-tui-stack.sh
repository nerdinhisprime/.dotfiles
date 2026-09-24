#!/bin/bash

install_tui_stack() {
  shopt -s dotglob nullglob

  for config in "$HOME/.dotfiles/home/.config/"*; do
    ln -snf "$config" "$HOME/.config/"
  done

  for file in "$HOME/.dotfiles/home/".*; do
    local name="$(basename "$file")"
    if [[ "$name" != "." && "$name" != ".." && "$name" != ".config" && "$name" != ".local" ]]; then
      ln -snf "$file" "$HOME/$name"
    fi
  done

  shopt -u dotglob nullglob

  sudo pacman -S --noconfirm --needed neovim yazi tmux btop fastfetch
}

install_gui_stack
