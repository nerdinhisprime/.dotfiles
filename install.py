#!/usr/bin/env python3
import subprocess
import inquirer
from pathlib import Path
import sys
import os
import shutil
import getpass

base_pkgs = [
    "zsh",
    "zsh-autosuggestions",
    "zsh-syntax-highlighting",
    "neovim",
    "git",
    "yazi",
    "zoxide",
    "eza",
    "openssh",
    "fastfetch",
    "curl",
    "stow",
]
font_pkgs = [
    "noto-fonts",
    "noto-fonts-cjk",
    "noto-fonts-emoji",
    "noto-fonts-extra",
    "ttf-dejavu",
    "ttf-liberation",
]
sys_pkgs = [
    "bluez",
    "bluez-utils",
    "bluetui",
    "pulsemixer",
    "pipewire",
    "pipewire-pulse",
    "pipewire-alsa",
    "wireplumber",
    "impala",
    "brightnessctl",
    "openh264",
    "btop",
]
desktop_pkgs = [
    "niri",
    "awww",
    "waybar",
    "foot",
    "pcmanfm",
    "mako",
    "wlsunset",
    "xdg-desktop-portal",
    "xdg-desktop-portal-gtk",
    "xdg-desktop-portal-gnome",
    "gnome-keyring",
]
dev_pkgs = ["tmux", "docker", "docker-compose", "npm"]
android_pkgs = ["gvfs", "gvfs-mtp", "libmtp", "android-udev", "scrcpy"]
nvidia_pkgs = ["nvidia-dkms", "nvidia-utils", "lib32-nvidia-utils"]
stow_links = [
    "zsh-core",
    "zsh-desktop",
    "tmux",
    "foot",
    "niri",
    "font",
    "bin",
    "mako",
    "user-dirs",
    "waybar",
]

categories = {
    "base": base_pkgs,
    "fonts": font_pkgs,
    "system": sys_pkgs,
    "desktop": desktop_pkgs,
    "dev": dev_pkgs,
    "android": android_pkgs,
    "nvidia": nvidia_pkgs,
}


def install_packages():
    print("\nInstalling packages!\n")
    questions = [
        inquirer.Checkbox(
            "selected_categories",
            message="change pkgs",
            choices=list(categories.keys()),
            default=list(categories.keys()),
        )
    ]
    answers = inquirer.prompt(questions)
    if not answers or not answers["selected_categories"]:
        print("no choce, exit.")
        return
    chosen = answers["selected_categories"]
    to_install = []
    for pkg in chosen:
        to_install.extend(categories[pkg])

    to_install = list(set(to_install))
    if not to_install:
        print("\nNo packages\n")
        return
    subprocess.run(
        ["bash", "./bash-scripts/package-installer.sh"] + to_install, check=True
    )


def create_links():
    print("\nCreating links!\n")
    subprocess.run(["bash", "./bash-scripts/create-simlinks.sh"], text=True)


def setup_docker():
    print("\nDocker setup...\n")
    subprocess.run(["bash", "./bash-scripts/setup-docker.sh"], text=True)


def setup_bluetooth():
    print("\nBluetooth setup...\n")
    subprocess.run(["bash", "./bash-scripts/setup-bluetooth.sh"], text=True)


def update_fonts_cache():
    print("\nUpdate font cache!\n")
    subprocess.run(["bash", "./bash-scripts/update-font-cache.sh"])


def change_shell():
    print("\nChanging shell!\n")
    subprocess.run(["bash", "./bash-scripts/change-shell.sh"], text=True)


def get_permissions_custom_scripts():
    print("\nGetting permissions for scripts from ~/.local/bin...\n")
    subprocess.run(["bash", "./bash-scripts/activate-custom-scripts.sh"], text=True)


def install_aur():
    print("\nInstall AUR installer\n")
    subprocess.run(["bash", "./bash-scripts/install-aur.sh"], text=True)


def setup_portals():
    print("\nInstall portals\n")
    subprocess.run(["bash", "./bash-scripts/setup-portals.sh"], text=True)


def main():
    create_links()
    get_permissions_custom_scripts()
    install_packages()
    install_aur()
    update_fonts_cache()
    setup_bluetooth()
    change_shell()
    setup_docker()
    setup_portals()
    print("\nSystem deployment complete! Reboot required\n")


if __name__ == "__main__":
    main()
