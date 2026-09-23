#!/bin/bash

setup_wifi() {
  sudo pacman -S --noconfirm --needed iwd dnscrypt-proxy impala nftables git

  sudo chattr -i /etc/resolv.conf 2>/dev/null || true

  sudo tee /etc/resolv.conf > /dev/null << 'EOF'
nameserver ::1
nameserver 127.0.0.1
options edns0
EOF

  sudo chattr +i /etc/resolv.conf

  sudo systemctl disable --now systemd-resolved
  sudo systemctl enable --now dnscrypt-proxy.service

  mkdir -p "$HOME/tool"
  git clone https://github.com/Sergeydigl3/zapret-discord-youtube-linux.git "$HOME/tool"
}

setup_wifi
