#!/bin/bash

change_shell() {
  sudo pacman -S --noconfirm --needed zsh zsh-autosuggestions zsh-syntax-highlighting eza zoxide

  for file in "$HOME/.dotfiles/home/".z*; do
    [[ -e "$file" ]] || continue

    local name="$(basename "$file")"
    ln -snf "$file" "$HOME/$name"
  done

  if [ "$SHELL" != "$(which zsh)" ]; then
    chsh -s "$(which zsh)"
  fi
}

change_shell
