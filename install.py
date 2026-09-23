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
desktop_pkgs = ["niri", "awww", "waybar", "foot", "pcmanfm", "mako"]
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
    cmd = ["sudo", "pacman", "-S", "--needed", "--noconfirm"] + to_install
    subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
    subprocess.run(cmd)


def create_links():
    print("\nCreating links!\n")
    subprocess.run(["sudo", "pacman", "-S", "stow", "--noconfirm"])
    home = Path.home()
    path_dotfiles = home / ".dotfiles"

    if not path_dotfiles.is_dir():
        print(f"There is not .dotfile directory at {path_dotfiles}")
        sys.exit(1)

    dirs = [".local/share/fonts", ".local/bin", ".config/nvim"]
    for directory in dirs:
        (home / directory).mkdir(parents=True, exist_ok=True)

    for link in stow_links:
        subprocess.run(["stow", "--restow", link], cwd=path_dotfiles, check=True)


def update_fonts_cache():
    print("\nUpdate font cache!\n")
    subprocess.run(["fc-cache", "-fv"])


def change_shell():
    print("\nChanging shell!\n")
    current_shell = os.environ.get("SHELL")
    zsh_path = shutil.which("zsh")

    if zsh_path and current_shell != zsh_path:
        print(f"Changing default shell to {zsh_path}...")
        subprocess.run(["sudo", "chsh", "-s", zsh_path, getpass.getuser()], check=True)


def setup_docker():
    print("\nDocker setup...\n")
    subprocess.run(["sudo", "systemctl", "enable", "--now", "docker.service"])
    subprocess.run(["sudo", "usermod", "-aG", "docker", getpass.getuser()])


def get_permissions_custom_scripts():
    print("\nGetting permissions for scripts from ~/.local/bin...\n")
    bin_dir = Path.home() / ".local/bin"

    if bin_dir.exists():
        for script in bin_dir.iterdir():
            if script.is_file():
                script.chmod(script.stat().st_mode | 0o111)

    subprocess.run(["sudo", "usermod", "-aG", "network", getpass.getuser()])


def setup_bluetooth():
    print("\nBluetooth setup\n")
    subprocess.run(["sudo", "systemctl", "enable", "--now", "bluetooth.service"])


def main():
    create_links()
    get_permissions_custom_scripts()
    install_packages()
    update_fonts_cache()
    setup_bluetooth()
    change_shell()
    setup_docker()
    print("\nSystem deployment complete! Reboot required\n")


if __name__ == "__main__":
    main()
