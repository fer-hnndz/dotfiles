# Based on Antonio Sarosi's dotfiles repo
# https://github.com/antoniosarosi/dotfiles

# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
import subprocess
from .theme_manager import ThemeManager

theme = ThemeManager("base").get_colors()


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.92, background=theme["background"])


screens = [Screen(top=status_bar(primary_widgets))]

# Autodetect available monitors and then set up the correct configuration
# NOTE: Should reload the configuration when a monitor is connected or disconnected
xrandr = "xrandr --auto && xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)


if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    print("Setting up a dual monitor...")

    subprocess.run(
        "xrandr --output HDMI-A-0 --primary --mode 1920x1080 --rate 100 --pos 1920x0 --rotate normal --output eDP --mode 1920x1080 --pos 0x0 --rotate normal --output DisplayPort-0 --off",
        shell=True,
    )

    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))
else:
    print("Setting up a single monitor...")
    subprocess.run(
        "xrandr --output HDMI-A-0 --off --output eDP --primary --mode 1920x1080 --pos 1912x0 --rotate normal --output DisplayPort-0 --off",
        shell=True,
    )
