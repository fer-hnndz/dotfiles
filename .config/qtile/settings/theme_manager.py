import json
import os


class ThemeManager:
    """Class that detects selected theme and loads the appropriate colors.

    Arguments
    ---------
    theme : str
        The name of the selected theme.
        Refer to themes.json for available themes.
    """

    def __init__(self, theme: str = "base"):
        self.theme = theme
        self.theme_data: dict = {}
        self._load_colors()

    def _load_colors(self) -> None:
        """Loads the selected color in the theme."""
        home = os.path.expanduser("~")
        with open(f"{home}/.config/qtile/themes.json", "r") as file:
            themes = json.load(file)
            self.theme_data = themes[self.theme]

    def get_bg(self) -> str:
        """Returns the background color."""
        return self.theme_data["background"]

    def get_fg(self) -> str:
        """Returns the foreground color."""
        return self.theme_data["foreground"]

    def get_powerline_colors(self) -> list[str]:
        """Returns the powerline colors."""
        return self.theme_data["powerline_colors"]
