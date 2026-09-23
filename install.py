#!/usr/bin/env python3
try:
    import questionary
except ImportError:
    print("Questionary is not found, run: yay -S python-questionary")
    exit(1)
from pathlib import Path
import subprocess


def main():
    bash_scripts = (Path.home() / ".dotfiles/bash-scripts").resolve()
    if bash_scripts.is_dir():
        file_names = [f.name for f in bash_scripts.glob("*.sh") if f.is_file()]

        selected_scripts = questionary.checkbox(
            "Change options:\n", choices=file_names
        ).ask()

        if selected_scripts:
            for f in selected_scripts:
                subprocess.run(["bash", str(bash_scripts / f)])


if __name__ == "__main__":
    main()
