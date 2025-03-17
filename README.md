# Dotfiles

This is a collection of configuration files for my Arch installation.

# Table of Contents

- [Window Manager and Login](#window-manager-and-login)
- [Setting up `dotfiles`](#setting-up-dotfiles)
- [Building the Basic Environment](#building-the-basic-environment)
  - [Wallpapers](#wallpapers)
  - [Audio](#audio)
    - [Equalizer](#equalizer)
  - [Brightness and Eye Care](#brightness-and-eye-care)
  - [Monitor Setup](#monitor-setup)
  - [Trackpad Gestures](#trackpad-gestures)
  - [Session Locker](#session-locker)
  - [Bluetooth](#bluetooth)
  - [SDDM](#sddm)
  - [Boot Screen](#boot-screen)
- [Extra Tools](#extra-tools)
  - [Program Launcher](#program-launcher)
  - [AUR Helper (yay)](#aur-helper-yay)
  - [Applets](#applets)
  - [Notification Support](#notification-support)
  - [OhMyZsh](#ohmyzsh)
- [Extra Software](#extra-software)
  - [Network Time Protocol (NTP)](#network-time-protocol-ntp)
  - [TRIM](#trim)
  - [Software](#software)

# Window Manager and Login

My preffered Window Manager is [**Hyprland**](https://wiki.archlinux.org/title/Hyprland). But I also use [**GNOME**](https://wiki.archlinux.org/title/GNOME) in case I want to use a more traditional desktop environment.

Before setting up the window manager, install some fonts to avoid issues.

```bash
$ sudo pacman -S ttf-dejavu ttf-liberation noto-fonts noto-fonts-cjk ttf-font-awesome
```

I also use some custom fonts, but these can be installed later:

- Mononoki (Nerd Font)
- Montserrat (_available on Google Fonts_)
- apple-fonts-ttf (AUR)
- ttf-segoe-ui (AUR)

## Installing GNOME

First I prefer to install GNOME since it avoids the hassle of setting up lots of stuff.

```bash
$ sudo pacman -S gdm gnome-shell gnome-terminal gnome-control-center gnome-menus evince xdg-desktop-portal-gnome gnome-keyring nautilus
```

Once that is done, enable GDM and restart your computer.

```bash
$ sudo systemctl enable gdm.service
```

You may now login into GNOME and tweak the settings to your liking.

## Setting up `dotfiles`

> [!IMPORTANT]
> To setup the dotfiles repository, make sure to setup Git properly.

Open a terminal and with a text editor edit your `.bashrc` file.

```bash
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

Once you have added the alias, clone the dotfiles repository

```bash
$ git clone --bare git@github.com:fer-hnndz/dotfiles.git $HOME/.dotfiles
$ dotfiles config --local status.showUntrackedFiles no
```

Now, proceed with the Hyprland installation before restoring the dotfiles.

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

You can now login into Hyprland and restore the dotfiles.

```bash
$ dotfiles checkout
```

I suggest to start editing `~/.config/hyprland/hyprland.conf` to your liking, in case you need to setup different monitors, input devices, etc.

> [!WARNING]
> To avoid having weird issues with text display, make sure to install the fonts mentioned above.
> You can now exit GNOME and login into Hyprland.

# Building the Basic Environment

In this section I'm going to details the tools I use in my Hyprland environment.\
GNOME should pretty much work out of the box.

## Wallpapers

To setup wallpapers, install [swww](https://github.com/LGFae/swww).

```bash
$ sudo pacman -S swww
```

> [!NOTE]
> swww's config is done on the Hyprland config file.
> You can also use `$ swww {path}` to set a wallpaper once the swww-daemon is running.

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

## Monitor Setup

Refer to Hyprland's [Monitor Setup](https://wiki.hyprland.org/Configuring/Monitors)

## Trackpad Gestures

Refer to Hyprland [Touchpad Settings](https://wiki.hyprland.org/Configuring/Variables/#touchpad)

## Session Locker

I use [hyprlock](https://github.com/hyprwm/hyprlock) to lock the session.

My configuration automatically invokes hyprlock when returning from a suspend.

```bash
$ sudo pacman -S hyprlock
```

To show the correct avatar, edit the avatar image to the correct path in the Hyprlock's config file.

## Bluetooth

I use `bluez` and `blueman` to manage bluetooth devices.

```bash
$ sudo pacman -S bluez blueman
$ sudo systemctl enable bluetooth.service
```

## Boot Screen

I use [Plymouth](https://wiki.archlinux.org/title/Plymouth) as my boot screen.

To apply the configuration, copy the file `plymouthd.conf` located in `extra-config` to `/etc/plymouth/`. \
Also, make sure to copy `mkinitcpio.conf` to `/etc/` and run `sudo mkinitcpio -P` to apply the changes.

# Extra Tools

In this section I'm going to detail some extra tools that I use in my Arch environment that speed up my workflow.

## Program Launcher

[Rofi](https://wiki.archlinux.org/title/Rofi) is a program launcher just like MacOS's Spotlight.\
Also install some icons so it looks better with the config.
You can install it with:

```bash
$ sudo pacman -S rofi papirus-icon-theme
```

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
sudo pacman -S mako
```

## OhMyZsh

I use `zsh` as my shell and `oh-my-zsh` as my configuration manager.\
To install `zsh` and `oh-my-zsh`:

```bash
$ sudo pacman -S zsh
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Install the `zsh-autosuggestions`, `zsh-syntax-highlighting` and `zsh-shift-select` plugins.

```bash
$ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

$ git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

$ git clone https://github.com/jirutka/zsh-shift-select.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-shift-select
```

# Extra Software

## Network Time Protocol (NTP)

To ensure clock is always correct, install `ntp`.

```bash
$ sudo pacman -S ntp
$ sudo systemctl enable ntpd.service
```

## TRIM

You can find TRIM utilities in `util-linux` package.

```bash
$ sudo pacman -S util-linux
$ sudo systemctl enable fstrim.timer
```

## Software

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
| galculator                    | Calculator                                     |
| filelight                     | Disk usage analyzer                            |
| evince                        | PDF viewer                                     |
| 7zip                          | 7zip                                           |
| mirage (AUR)                  | Image Viewer                                   |
| dbvis                         | Database Visualizer Tool                       |
