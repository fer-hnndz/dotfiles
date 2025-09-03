"""
HHDR Controller v0.1

CLI tool to change HDR settings on external monitors.
By: Jorge F. Hernández
"""

from pathlib import Path
import argparse

HYPRLAND_CONFIG_PATH = Path("~/.config/hypr/hyprland.conf").expanduser()
verbose = False


def _get_current_hdr_status():
    with open(HYPRLAND_CONFIG_PATH, "r", encoding="utf-8") as f:
        lines = filter(lambda s: s.startswith("monitor"), f.readlines())

        for line in lines:
            line = line.strip()

            if "cm," in line:
                if "cm, hdr" in line:
                    return True
                else: return False

        return False


def _set_hdr_status(status: bool):
    with open(HYPRLAND_CONFIG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(HYPRLAND_CONFIG_PATH, "w", encoding="utf-8") as f:
        contents = ""

        for line in lines:
            if "cm," in line:
                if status:
                    line = line.replace("cm, srgb#", "cm, hdr")
                else:
                    line = line.replace("cm, hdr", "cm, srgb#")

            # print(line)
            contents += line

        f.write(contents)


parser = argparse.ArgumentParser(
    prog="HHDR Controller",
    description="Simple CLI to control HDR settings on your Hyprland's config file.",
    epilog="-== Made by Jorge F. Hernández ==-",
)
parser.add_argument(
    "command", nargs="?", choices=["status", "set"], help="Command to execute"
)
parser.add_argument(
    "value", nargs="?", choices=["on", "off"], help="Value for set command"
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Enable verbose output",
)


def entry_point(args):
    current_status = _get_current_hdr_status()

    if args.verbose and args.command != "status":
        print("Current HDR status:", "Enabled" if current_status else "Disabled")

    if args.command == "status":
        print("Current HDR status:", "Enabled" if current_status else "Disabled")
        return

    if args.command == "set":
        if args.value is None:
            print("Error: 'set' command requires a value (on/off)")
            return

        if args.value == "on":
            target_status = True
        elif args.value == "off":
            target_status = False
        else:
            print("Error: Invalid value for 'set' command (on/off)")
            return

        if current_status == target_status:
            print("HDR is already", "on." if current_status else "off.")
        else:
            _set_hdr_status(target_status)
            print("HDR set to", "on." if target_status else "off.")
        return

    # Handle no command (toggle)
    if args.command is None:
        target_status = not current_status
        _set_hdr_status(target_status)
        print("HDR toggled to", "on." if target_status else "off.")


if __name__ == "__main__":
    entry_point(parser.parse_args())
