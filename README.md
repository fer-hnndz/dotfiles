# Dotfiles

This is a collection of configuration files for my Arch installation.

Special thanks to [@AntonioSarosi](https://github.com/antoniosarosi/dotfiles) who I reffered from to make my own QTile configuration and other program choices.

# Table of Contents
- [Post Arch Installation](#post-arch-installation)
- [QTile and Login](#qtile-and-login)
- [Useful Programs](#useful-programs)
    - [Program Launcher](#program-launcher)
    - [AUR Helper](#aur-helper)
    - [Wallpapers](#wallpapers)
    - [Brightness](#brightness)
    - [Monitor Setup](#monitor-setup)
    - [Applets](#applets)
    - [Notification Support](#notification-support)
    - [Touchpad Gestures](#touchpad-gestures)

# Post Arch Installation
After installing Arch on the live USB make sure you have installed some utilites for later.

```bash
pacman -S networkmanager nano sudo git
systemctl enable networkmanager.service

# Make sure to setup correctly the sudoers file and add the your user to it.

# Use nano (my preffered console text editor) to edit the sudoers file.
export EDITOR=nano;
visudo
```

You can later setup the network easier with `nmtui`.

For the bootloader I chose `rEFInd` since it was a less pain in the ass experience that GRUB.\
Refer to [rEFInd Installation](https://wiki.archlinux.org/title/REFInd).\
*Note for myself: When I first installed rEFInd, I had an issue where the rEFInd installation script will attempt to mount the live USB, resulting that whenever I tried to run without the USB, Arch won't boot.*

# QTile and Login

My to-go Window Manager is QTile. Simple enough for me.\
It may happen that some fonts are not displayed correctly, to fix this try to install some fonts:

```bash
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
```

To install all the useful stuff to setup QTile we need a LightDM, a greeter, a text editor (in case not installed), `xterm` since that is what QTile use by default.

```
sudo pacman -S lightdm lightdm-gtk-greeter qtile xterm firefox
sudo systemctl enable lightdm

# You may want to reboot so ligthdm launches QTile on the next boot.
systemctl reboot
```

Quit QTile with `mod+shift+q` and relaunch it to load the fonts.

# Useful Programs

## Program Launcher
Rofi is a program launcher just like MacOS's Spotlight.\
You can install it with:
```
sudo pacman -S rofi
```

## AUR Helper

To avoid all the hassle of building and installing packages from the AUR, I suggest to install `yay` to simplify those tasks.

Install the necessary tools for building packages and then clone the yay git repo.
```
sudo pacman -S base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg
```

## Wallpapers

For the wallpapers I prefer using `nitrogen`.
```
sudo pacman -S nitrogen
nitrogen /path/to/wallpapers/dir
# Will open a window that allows you to pick a wallpaper even for different screens.

# To restore the last used wallpapers simply run
nitrogen --restore &
```

## Audio
Imagine using Arch with no audio. Impossible. Get some audio:

```
sudo pacman -S pulseaudio pavucontrol pamixer
```

`pulseaudio` will allow for audio support while `pavucontrol` and `pamixer` offer a GUI and CLI setup respectively.

## Brightness

You may be usong a laptop, so to save some battery consider controlling the screen brightness.

```
sudo pacman -S brightnessctl
```

## Monitor Setup
`xrandr` allows for CLI support to edit monitor orientation.
My QTile config automatically setups the monitor positions based on how I currently used my laptop and monitor. \
To install both tools:

```
sudo pacman -S xorg-xrandr arandr
```

If you ever want to change the monitor orientation, use `arandr` and copy the script for `xrandr`. 

## Applets
wip

## Notification Support
wip








