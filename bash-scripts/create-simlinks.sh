#!/bin/bash

create_simlinks() {
  local bin="$HOME/.local/bin"

  mkdir -p "$HOME/.config" "$bin"

  shopt -s dotglob nullglob

  for file in "$HOME/.dotfiles/home/".*; do
    local name="$(basename "$file")"
    if [[ "$name" != "." && "$name" != ".." && "$name" != ".config" && "$name" != ".local" ]]; then
      ln -snf "$file" "$HOME/$name"
    fi
  done

  if [[ -d "$HOME/.dotfiles/home/.local/bin" ]]; then
    for b in "$HOME/.dotfiles/home/.local/bin/"*; do
      ln -snf "$b" "$bin/"
    done
  fi

  shopt -u dotglob nullglob
}

create_simlinks
