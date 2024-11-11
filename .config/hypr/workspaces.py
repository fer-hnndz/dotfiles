import subprocess
import re
import sys


def parse_workspaces():
    # Run `hyprctl workspaces` and capture the output
    result = subprocess.run(["hyprctl", "workspaces"], capture_output=True, text=True)
    output = result.stdout

    # Dictionary to hold workspace ID to monitor ID mappings
    workspaces = {}

    # Use regular expressions to find each workspace block
    matches = re.findall(r"workspace ID (\d+).+?monitorID: (\d+)", output, re.DOTALL)

    # Populate the dictionary with workspaceId as key and monitorId as value
    for workspace_id, monitor_id in matches:
        workspaces[int(workspace_id)] = int(monitor_id)

    return workspaces


def get_current_monitor_id():
    # Run the `hyprctl activeworkspace` command
    result = subprocess.run(
        ["hyprctl", "activeworkspace"], capture_output=True, text=True
    )

    # Search for the line containing `monitorID: X`
    match = re.search(r"monitorID:\s*(\d+)", result.stdout)

    if match:
        # Return the value of X as an integer
        return int(match.group(1))
    else:
        # If the pattern is not found, return None or a default value
        return None


# Execute the parser and print the result

selected_workspace = int(sys.argv[1])
workspaces = parse_workspaces()
current_monitor_id = get_current_monitor_id()

if selected_workspace in workspaces:
    if workspaces[selected_workspace] != current_monitor_id:
        # Switch workspace to the selected monitor
        subprocess.run(["hyprctl", "switchworkspace", str(selected_workspace)])
    else:
        print("No action needed")
