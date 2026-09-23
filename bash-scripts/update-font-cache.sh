#!/bin/bash

update-font-cache() {
  sudo pacman -S --noconfirm --needed noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra ttf-dejavu ttf-liberation

  local fonts="$HOME/.local/share/fonts"
  mkdir -p "$fonts"

  shopt -s dotglob nullglob

  if [[ -d "$HOME/.dotfiles/home/.local/share/fonts" ]]; then
    for f in "$HOME/.dotfiles/home/.local/share/fonts/"*; do
      ln -snf "$f" "$fonts/"
    done
  fi

  shopt -u dotglob nullglob

  fc-cache -fv
}

update-font-cache
