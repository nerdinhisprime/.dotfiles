#!/bin/bash

change_shell() {
  if [ "$SHELL" != "$(which zsh)" ]; then
    chsh -s $(which zsh)
  fi
}

change_shell
