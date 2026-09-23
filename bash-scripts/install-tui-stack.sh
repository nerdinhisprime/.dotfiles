#!/bin/bash

install_tui_stack() {
  shopt -s dotglob nullglob

  for config in "$HOME/.dotfiles/home/.config/"*; do
    ln -snf "$config" "$HOME/.config/"
  done

  shopt -u dotglob nullglob

  sudo pacman -S --noconfirm --needed neovim yazi tmux btop fastfetch
}

install_gui_stack
