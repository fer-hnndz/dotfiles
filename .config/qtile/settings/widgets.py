from libqtile import widget


widget_defaults = {
    "font": "Mononoki Nerd Font",
    "fontsize": 18,
    "padding": 3,
}

widgets = [
    # widget.CurrentLayout(),
    widget.GroupBox(),
    widget.Prompt(),
    # widget.WindowName(),
    # widget.Chord(
    #     chords_colors={
    #         "launch": ("#ff0000", "#ffffff"),
    #     },
    #     name_transform=lambda name: name.upper(),
    # ),
    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
    # widget.StatusNotifier(),
    widget.Systray(),
    widget.Clock(format="%d/%m/%y %H:%M"),
    widget.Battery(
        charge_controller=lambda: (0, 90),
        charge_char="^",
        discharge_char="~",
        font="mono",
        format="| Battery: {char} {percent:2.0%} |",
    ),
]
