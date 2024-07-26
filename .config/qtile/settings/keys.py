from libqtile.config import Key
from libqtile.lazy import lazy

terminal = "alacritty"
mod = "mod4"
alt = "mod1"

keys = [
    Key(modifier, key, command, desc=desc)
    for modifier, key, command, desc in [
        # Window Movement
        ([mod], "j", lazy.layout.shuffle_left(), "Move Window Left"),
        ([mod], "l", lazy.layout.shuffle_right(), "Move Window Right"),
        ([mod], "s", lazy.layout.shuffle_down(), "Move Window Down"),
        # App Launch
        ([mod], "Return", lazy.spawn(terminal), "Spawn a Terminal"),
        ([mod], "w", lazy.window.kill(), "Kill Window"),
        ([alt], "space", lazy.spawn("rofi -show window"), "Opens Rofi"),
        # QTile Binds
        ([mod, "control"], "r", lazy.reload_config(), "Reload the config"),
        ([mod, "control"], "q", lazy.shutdown(), "Shutdown Qtile"),
        ([mod], "r", lazy.spawncmd(), "Spawn a command using a prompt widget"),
        ([mod], "Tab", lazy.next_layout(), "Toggle between layouts"),
        (
            [mod],
            "f",
            lazy.window.toggle_fullscreen(),
            "Toggle fullscreen",
        ),
        # Audio
        # Volume
        (
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pamixer --decrease 5"),
            "Lower Volume",
        ),
        (
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pamixer --increase 5"),
            "Raise Volume",
        ),
        ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"), "Mute Audio"),
    ]
]
