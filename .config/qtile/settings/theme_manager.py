import json
import os
from typing import TypedDict


class ThemeDict(TypedDict):
    background: str
    foreground: str
    group_bg: str
    active_group_fg: str
    active_group_bg: str
    powerline_colors: list[str]
    urgent_bg: str
    urgent_fg: str


class ThemeManager:
    """Class that detects selected theme and loads the appropriate colors.

    Arguments
    ---------
    theme : str
        The name of the selected theme.
        Refer to themes.json for available themes.
    """

    def __init__(self):
        self.theme = "chrome" # Select theme here
        self.theme_data: dict = {}
        self._load_colors()

    def _load_colors(self) -> None:
        """Loads the selected color in the theme."""
        home = os.path.expanduser("~")
        with open(f"{home}/.config/qtile/themes.json", "r") as file:
            themes = json.load(file)
            self.theme_data = themes[self.theme]

    def get_colors(self) -> ThemeDict:
        """Returns the colors for the selected theme."""
        return self.theme_data  # type: ignore
