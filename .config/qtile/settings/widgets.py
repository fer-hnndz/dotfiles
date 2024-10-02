from libqtile import widget
from .theme_manager import ThemeManager

widget_defaults = {
    "font": "Mononoki Nerd Font Bold",
    "fontsize": 16,
    "padding": 3,
}

theme = ThemeManager().get_colors()

# ============= Widget Functions =============


def powerline(fg=theme["foreground"], bg=theme["background"]):
    return widget.TextBox(
        foreground=fg,
        background=bg,
        text="󰍞",  # 
        fontsize=70,
        padding=-14,  # Icon: nf-oct-triangle_left
    )

def separator():
    return widget.Sep(
        linewidth=0,
        padding=6,
    )


def groups():
    return (
        widget.GroupBox(
            highlight_method="block",
            background=theme["group_bg"],
            active=theme["active_group_fg"],
            inactive=theme["foreground"],
            spacing=20,
            fontsize=20,
            disable_drag=True,
            rounded=False,
            this_current_screen_border=theme["active_group_bg"],
            this_screen_border=theme["active_group_bg"],
            other_current_screen_border=theme["active_group_bg"],
            other_screen_border=theme["active_group_bg"],
            urgent_alert_method="block",
            urgent_border=theme["urgent_bg"],
            urgent_text=theme["urgent_fg"],
            fmt=" {}  ",
        ),
        widget.WindowName(),
    )


primary_widgets = [
    *groups(),
    widget.Spacer(),

    # System Tray
    powerline(fg=theme["powerline_colors"][2], bg=theme["background"]),
    widget.Systray(background=theme["powerline_colors"][2]),

    # Layout Powerline
    powerline(fg=theme["powerline_colors"][3]),
    widget.TextBox(background=theme["powerline_colors"][3], text=" ", fontsize=20),
    widget.CurrentLayout(background=theme["powerline_colors"][3]),

    # Battery Powerline
    powerline(bg=theme["background"], fg=theme["powerline_colors"][0]),
    widget.Battery(
        charge_controller=lambda: (0, 90),
        charge_char="󰂄",
        discharge_char="󰂍",
        font="mono",
        format=" {char} {percent:2.0%} ",
        background=theme["powerline_colors"][0],
    ),
    # Clock Powerline
    powerline(bg=theme["background"], fg=theme["powerline_colors"][1]),
    widget.Clock(format="%d/%m/%y %H:%M", background=theme["powerline_colors"][1]),
]

secondary_widgets = [
    *groups(),
    widget.Spacer(),

    # Layout Powerline
    powerline(fg=theme["powerline_colors"][3]),
    widget.TextBox(background=theme["powerline_colors"][3], text=" ", fontsize=20),
    widget.CurrentLayout(background=theme["powerline_colors"][3]),
 
    # Battery Powerline
    powerline(bg=theme["background"], fg=theme["powerline_colors"][0]),
    widget.Battery(
        charge_controller=lambda: (0, 90),
        charge_char="󰂄",
        discharge_char="󰂍",
        font="mono",
        format=" {char} {percent:2.0%} ",
        background=theme["powerline_colors"][0],
    ),

    # Clock Powerline
    powerline(bg=theme["background"], fg=theme["powerline_colors"][1]),
    widget.Clock(format="%d/%m/%y %H:%M", background=theme["powerline_colors"][1]),
]
