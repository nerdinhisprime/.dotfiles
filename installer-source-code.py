from pathlib import Path
import subprocess

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.events import Key
from textual.widgets import SelectionList, Static
from textual.widgets.selection_list import Selection


class ScriptPicker(App):
    CSS = """
    Horizontal { height: 1fr; }
    SelectionList { width: 50%; }
    """

    def __init__(self, scripts: list[Path]):
        super().__init__()
        self.scripts = scripts

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield SelectionList[Path](
                *[Selection(s.name, s) for s in self.scripts]
            )
            yield Static(id="preview")

    def on_selection_list_selection_highlighted(
        self, event: SelectionList.SelectionHighlighted
    ) -> None:
        path: Path = event.selection.value
        try:
            self.query_one("#preview", Static).update(path.read_text(encoding="utf-8"))
        except Exception as e:
            self.query_one("#preview", Static).update(f"Ошибка чтения: {e}")

    def on_key(self, event: Key) -> None:
        sel_list = self.query_one(SelectionList)

        if event.key == "j":
            sel_list.action_cursor_down()
            event.prevent_default()
            event.stop()
        elif event.key == "k":
            sel_list.action_cursor_up()
            event.prevent_default()
            event.stop()

        elif event.key == "enter":
            event.prevent_default()
            event.stop()
            self.exit(list(sel_list.selected))


if __name__ == "__main__":
    bash_scripts = (Path.home() / ".dotfiles/bash-scripts").resolve()

    if bash_scripts.is_dir():
        scripts = sorted(f for f in bash_scripts.glob("*.sh") if f.is_file())
        app = ScriptPicker(scripts)
        selected_paths = app.run()

        if selected_paths:
            print(f"\nЗапуск выбранных скриптов ({len(selected_paths)} шт.):")
            for path in selected_paths:
                print(f"-> Выполнение {path.name}...")
                subprocess.run(["bash", str(path)])
