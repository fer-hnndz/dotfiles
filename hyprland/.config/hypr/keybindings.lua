---------------
---- INPUT ----
---------------

hl.config({
	input = {
		kb_layout = "us, us",
		kb_variant = "basic, intl",
		kb_model = "",
		kb_options = "grp:alt_shift_toggle",
		kb_rules = "",

		follow_mouse = 1,
		accel_profile = "flat",
		sensitivity = 0.05,

		touchpad = {
			natural_scroll = true,
			scroll_factor = 0.6,
		},
	},
})

hl.gesture({
	fingers = 3,
	direction = "horizontal",
	action = "workspace",
})

---------------------
---- MY PROGRAMS ----
---------------------

local terminal = "kitty"
local fileManager = "thunar"
local menu = "/home/fer/.config/rofi/scripts/launcher_t1"
local powerMenu = "/home/fer/.config/rofi/scripts/powermenu_t2"

---------------------
---- KEYBINDINGS ----
---------------------

local mainMod = "SUPER"

hl.bind(mainMod .. " + Return", hl.dsp.exec_cmd(terminal)) -- Open a terminal
hl.bind(mainMod .. " + P", hl.dsp.exec_cmd(powerMenu)) -- Powermenu
hl.bind(mainMod .. " + L", hl.dsp.exec_cmd("hyprlock")) -- Lock computer
hl.bind(mainMod .. " + TAB", hl.dsp.window.fullscreen({ mode = "maximized", action = "toggle" })) -- Toggle maximize a window
hl.bind(mainMod .. " + F", hl.dsp.window.fullscreen({ mode = "fullscreen", action = "toggle" })) -- Toggle fullscreen a window
hl.bind(mainMod .. " + W", hl.dsp.window.close()) -- Close a window
hl.bind(
	mainMod .. " + M",
	hl.dsp.exec_cmd("command -v hyprshutdown >/dev/null 2>&1 && hyprshutdown || hyprctl dispatch 'hl.dsp.exit()'")
) -- Exit Hyprland
hl.bind(mainMod .. " + E", hl.dsp.exec_cmd(fileManager)) -- Open File Manager
hl.bind(mainMod .. " + V", hl.dsp.window.float({ action = "toggle" })) -- Toggle Floating Window
hl.bind("ALT + Space", hl.dsp.exec_cmd(menu)) -- Open Rofi Launcher

-- Switch workspaces with mainMod + [0-9]
-- Move active window to a workspace with mainMod + SHIFT + [0-9]
for i = 1, 10 do
	local key = i % 10 -- 10 maps to key 0
	hl.bind(mainMod .. " + " .. key, hl.dsp.focus({ workspace = i, on_current_monitor = true }))
	hl.bind(mainMod .. " + SHIFT + " .. key, hl.dsp.window.move({ workspace = i }))
end

-- Special Workspace
hl.bind(mainMod .. " + S", hl.dsp.workspace.toggle_special("magic"))
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.window.move({ workspace = "special:magic" }))

-- Move/resize windows with mainMod + LMB/RMB and dragging
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })

-- Laptop multimedia keys for volume and LCD brightness
hl.bind(
	"XF86AudioRaiseVolume",
	hl.dsp.exec_cmd("swayosd-client --output-volume raise"),
	{ locked = true, repeating = true }
)
hl.bind(
	"XF86AudioLowerVolume",
	hl.dsp.exec_cmd("swayosd-client --output-volume lower"),
	{ locked = true, repeating = true }
)
hl.bind(
	"XF86AudioMute",
	hl.dsp.exec_cmd("swayosd-client --output-volume mute-toggle"),
	{ locked = true, repeating = true }
)

hl.bind(
	"XF86MonBrightnessUp",
	hl.dsp.exec_cmd("swayosd-client --brightness raise"),
	{ locked = true, repeating = true }
)
hl.bind(
	"XF86MonBrightnessDown",
	hl.dsp.exec_cmd("swayosd-client --brightness lower"),
	{ locked = true, repeating = true }
)
