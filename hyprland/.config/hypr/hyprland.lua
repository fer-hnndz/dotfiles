require("theming")
require("keybindings")
------------------
---- MONITORS ----
------------------

-- See https://wiki.hypr.land/Configuring/Basics/Monitors/
hl.monitor({
    output = "desc:IWB PC Monitor",
    mode = "preferred",
    position = "auto",
    scale = 2,
    mirror = "eDP-1",
})

hl.monitor({
    output = "desc:JVC LT-MK24220",
    mode = "1920x1080@100.0",
    position = "1600x0",
    scale = 1,
    bitdepth = 10,
})

hl.monitor({
    output = "eDP-1",
    mode = "1920x1080@60.01",
    position = "0x180",
    scale = 1.2,
})

hl.monitor({
    output = "",
    mode = "preffered",
    position = "auto",
    scale = 1,
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
