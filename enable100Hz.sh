#!/bin/zsh
# © Jorge F. Hernández, 2024

# I made this script so I can automate the process of enabling 100Hz on my main monitor,
# since I won't always need the 100Hz.

# The values after the mode name are specific to what Xorg logs based on driver's desired resolution.
# For more info, refer to:
# https://wiki.archlinux.org/title/Xrandr#Adding_undetected_resolutions

xrandr --newmode "1920x1080_100.00" 229.54 1920 1968 2000 2035 1080 1083 1088 1128 +hsync +vsync
xrandr --addmode HDMI-A-0 1920x1080_100.00
