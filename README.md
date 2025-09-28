# Dotfiles

This is a collection of configuration files for my Arch installation.

Clone this repository with git and follow the guide below.

# Window manager and Desktop Experience

My go-to choice is [**Hyprland**](https://wiki.archlinux.org/title/Hyprland).
Before setting up the window manager, install some fonts to avoid issues.

```bash
$ sudo pacman -S ttf-dejavu ttf-liberation noto-fonts noto-fonts-cjk ttf-font-awesome
```

I also use some custom fonts, but these can be installed later:

- Mononoki (Nerd Font)
- apple-fonts-ttf (AUR)
- ttf-segoe-ui (AUR)

You may now login into GNOME and tweak the settings to your liking.

## Setting up `dotfiles` and `stow`

Make sure you have `stow` installed beforehand. \
Head over to the root of the repository, you can see different config folders for my setup.

If you want to copy the configuration for Hyprland for instance, run:

```bash
stow hypr-laptop
```

This will create the symlinks to my Hyprland's settings.

## Installing Hyprland

First, install Hyprland and some other tools for suspending, locking, screenshots, etc. and its dependencies.

```bash
# Terminal
$ sudo pacman -S kitty

# Hyprland
$ sudo pacman -S hyprland hypridle hyprlock hyprshot hyprutils hyprpolkitagent waybar qt5-wayland qt6-wayland xdg-desktop-portal-hyprland qt5-graphicaleffects qt5-quickcontrols2

# Clipboard tools
$ sudo pacman -S wl-clipboard cliphist
```

You can now login into Hyprland and stow more configs.

I suggest to start editing `~/.config/hyprland/hyprland.conf` to your liking, in case you need to setup different monitors, input devices, etc.

> [!WARNING]
> To avoid having weird issues with text display, make sure to install the fonts mentioned above.

# Building the Basic Environment

In this section I'm going to details the tools I use in my Hyprland environment.\
GNOME should pretty much work out of the box.

## File manager

I use Gnome's **Nautilus** file explorer.
I also install the following to render thumbnails correctly.

```bash
sudo pacman -S ffmpegthumbnailer gst-libav gst-plugins-ugly ffmpeg-audio-thumbnailer
```

## Wallpapers

To setup wallpapers, install [swww](https://github.com/LGFae/swww).

```bash
$ sudo pacman -S swww
```

## Audio

I use [Pipewire](https://wiki.archlinux.org/title/PipeWire) for audio.
Refer to the installation guide for setup details.

```bash
$ sudo pacman -S pipewire pipewire-audio pipewire-pulse pipewire-alsa pipewire-jack
```

To add control via CLI or GUI install `pamixer` and`pavucontrol` respectively.

```bash
$ sudo pacman -S pavucontrol pamixer
```

Installing and rebooting should be enough to get audio working.

### Equalizer

I use `EasyEffects`. \
I've also included some presets in the `extra-config` folder. \
To apply the presets, move them to `~/.config/easyeffects/output` and select them in the EasyEffects GUI.

For equalizer effects to work, install EasyEffects and the required plugins:

```bash
$ sudo pacman -S easyeffects calf lsp-plugins
```

## Brightness and Eye Care

To control the brightness of the screen, you can use `brightnessctl`.\
You can also install [wlsunset](https://github.com/kennylevinsen/wlsunset) to control the color temperature of your screen.

```bash
$ sudo pacman -S brightnessctl wlsunset
$ wlsunset -l LAT -L LON
```

wlsunset is setup in Hyprland's config file. You can change the location and the color temperature to your liking.

## Session Locker

I use [hyprlock](https://github.com/hyprwm/hyprlock) to lock the session.
My configuration automatically invokes hyprlock when returning from a suspend.

```bash
$ sudo pacman -S hyprlock
```

## Bluetooth

I use `bluez` and `blueman` to manage bluetooth devices.

```bash
$ sudo pacman -S bluez blueman
$ sudo systemctl enable bluetooth.service
```

## Boot Screen

I use [Plymouth](https://wiki.archlinux.org/title/Plymouth) as my boot screen.

## Program Launcher

[Rofi](https://wiki.archlinux.org/title/Rofi) is a program launcher just like MacOS's Spotlight.\
Also install some icons so it looks better with the config.
You can install it with:

```bash
$ sudo pacman -S rofi papirus-icon-theme
```

## Volume and Caps OSD

I use [swayosd](https://github.com/ErikReider/SwayOSD) to show my current volume and caps lock status.

## AUR Helper (yay)

To avoid all the hassle of building and installing packages from the AUR, I suggest to install `yay` to simplify those tasks.

Install the necessary tools for building packages and then clone the yay git repo.

```bash
$ sudo pacman -S base-devel
$ git clone https://aur.archlinux.org/yay.git
$ cd yay
$ makepkg -si
```

## Applets

Easily control the network with an applet.

```bash
$ sudo pacman -S network-manager-applet
```

## Notification Support

With Hyprland no further notification setup is needed aside from installing a notification daemon.

```bash
sudo pacman -S swaync
```

## OhMyZsh

I use `zsh` as my shell and `oh-my-zsh` as my configuration manager.\
My selected theme is `gnzh`.\
To install `zsh` and `oh-my-zsh`:

```bash
$ sudo pacman -S zsh
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Install the `zsh-autosuggestions`, `zsh-syntax-highlighting` and `zsh-shift-select` plugins.\

```bash
$ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

$ git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

$ git clone https://github.com/jirutka/zsh-shift-select.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-shift-select
```

# Extra Software

Below is the rest of programs that I use that don't need detailed explanation or configuration.

| Software                      | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| Less                          | Pager for Git and Arch journal                 |
| visual-studio-code-bin (AUR)  | Propietary VsCode (for extension sync support) |
| spotify (AUR)                 | ¯\_(ツ)\_/¯                                    |
| Discord                       | Chat                                           |
| NeoVim                        | Text editor                                    |
| Firefox                       | Web browser                                    |
| Gedit                         | Simple graphical text editor                   |
| obs-studio (Flatpak)          | Screen recording                               |
| Droidcam OBS Plugin (Flatpak) | Android camera plugin for OBS                  |
| btop                          | System monitor                                 |
| postman-bin (AUR)             | API testing tool                               |
| cmatrix                       | Matrix screensaver                             |
| gnome-calculator              | Calculator                                     |
| filelight                     | Disk usage analyzer                            |
| evince                        | PDF viewer                                     |
| 7zip                          | 7zip                                           |
| Loupe                         | Image Viewer                                   |
| dbvis                         | Database Visualizer Tool                       |
| bleachbit                     | System Cleaner                                 |
