#!/usr/bin/env python3
try:
    import questionary
except ImportError:
    print("questionary lib not found. run: yay -S python-questionary")
    exit(1)

checkbox = questionary.checkbox(
    "which packages install?", choices=["base", "niri", "dev", "games", "docker"]
).ask()

select = questionary.select("change distro:", choices=["arch", "wsl", "termux"]).ask()

text = questionary.text("hostname: ", default="arch-laptop").ask()

if not questionary.confirm('run install?', default=True).ask():
    print('chlen')
    exit(1)

print(checkbox, select, text)
