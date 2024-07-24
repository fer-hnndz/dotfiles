from libqtile import widget
from .theme_manager import ThemeManager

widget_defaults = {
    "font": "Mononoki Nerd Font Bold",
    "fontsize": 20,
    "padding": 3,
}


mgr = ThemeManager("base")


def powerline(fg="#FFFFFF", bg="#FF0000"):
    return widget.TextBox(
        foreground=fg,
        background=bg,
        text="",
        fontsize=82,
        padding=-2,  # Icon: nf-oct-triangle_left
    )


def separator():
    return widget.Sep(
        linewidth=0,
        padding=6,
    )


widgets = [
    widget.GroupBox(
        spacing=20,
        highlight_method="block",
        block_highlight_text_color=mgr.get_fg(),
    ),
    widget.Prompt(),
    widget.CurrentLayout(),
    widget.Spacer(),
    powerline(bg=mgr.get_bg(), fg=mgr.get_powerline_colors()[0]),
    widget.Battery(
        charge_controller=lambda: (0, 90),
        charge_char="󰂄",
        discharge_char="󰂍",
        font="mono",
        format=" {char} {percent:2.0%} ",
        background=mgr.get_powerline_colors()[0],
    ),
    # widget.WindowName(),
    powerline(bg=mgr.get_bg(), fg=mgr.get_powerline_colors()[1]),
    widget.Clock(format="%d/%m/%y %H:%M", background=mgr.get_powerline_colors()[1]),
]
