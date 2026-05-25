require("theming")
require("keybindings")
require("monitors")
------------------------
---- WINDOW RULES ------
------------------------
hl.window_rule({
    name = "center-pacsea",
    match = {
        initial_title = "pacsea"
    },
    float = true,
    size = {"monitor_w*0.9", "monitor_h*0.8"},
    center = true,
    pin = true,
    stay_focused=true

})
-------------------
---- AUTOSTART ----
-------------------
hl.on("hyprland.start", function()
    hl.exec_cmd("nm-applet")
    hl.exec_cmd("blueman-applet")
    hl.exec_cmd("waybar")
    hl.exec_cmd("awww-daemon")
    hl.exec_cmd("easyeffects --gapplication-service")
    hl.exec_cmd("hypridle")
    hl.exec_cmd("systemctl --user start hyprpolkitagent")
    hl.exec_cmd("wlsunset -l 15 -L -88 -T 6000")
    hl.exec_cmd("wl-paste --watch cliphist store")
    hl.exec_cmd("/usr/lib/polkit-kde-authentication-agent-1")
    hl.exec_cmd("swayosd-server")
end)
