# Dotfiles

This is a collection of configuration files for my Arch installation.


# Table of Contents
- [Post Arch Installation](#post-arch-installation)
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
  - [Boot Screen](#boot-screen)
- [Extra Tools](#extra-tools)
  - [Program Launcher](#program-launcher)
  - [AUR Helper (yay)](#aur-helper-yay)
  - [Applets](#applets)
  - [Notification Support](#notification-support)
  - [OhMyZsh](#ohmyzsh)
- [Extra Software](#extra-software)


# Post Arch Installation
After installing Arch on the live USB make sure you have installed some utilites for later.

```bash
$ pacman -S networkmanager neovim sudo git
$ systemctl enable networkmanager.service

# Make sure to setup correctly the sudoers file and add the your user to it.

$ export EDITOR=nvim;
$ visudo
```

You can later setup the network easier with `nmtui`.

For the bootloader I chose `rEFInd` since it was a smoother experience setting it up.
Refer to [rEFInd Installation](https://wiki.archlinux.org/title/REFInd).

# Window Manager and Login

Before setting up the window manager, install some fonts to avoid issues.

```bash
$ sudo pacman -S ttf-dejavu ttf-liberation noto-fonts noto-fonts-cjk ttf-font-awesome
```

Also install firefox and unzip tool to download the Mononoki font.

```bash
$ sudo pacman -S firefox unzip

# After downloading Mononoki
$ unzip Mononoki.zip -d Mononoki
$ mkdir ~/.local/share/fonts/ttf
$ cp Mononoki ~/.local/share/fonts/ttf
```

My setup is:
- [Hyprland](https://wiki.archlinux.org/title/Hyprland) (Window Manager)
- [SDDM](https://wiki.archlinux.org/title/SDDM) (Login Manager)
- [kitty](https://wiki.archlinux.org/title/Kitty) (Terminal)

```bash
$ sudo pacman -S hyprland sddm kitty waybar qt5-wayland qt6-wayland wl-clipboard xdg-desktop-portal-hyprland qt5-graphicaleffects qt5-quickcontrols2
$ sudo systemctl enable sddm.service

# You may want to reboot so ligthdm launches Hyprland on the next boot.
$ systemctl reboot
```

## Setting up `dotfiles`

Once rebooted, login into your user and you should see Hyprland.
Open a terminal and with a text editor edit your `.bashrc` file.

```bash
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

Once you have added the alias, clone the dotfiles repository. \
**Make sure you've set up your SSH keys for GitHub.**

```bash
$ git clone --bare git@github.com:fer-hnndz/dotfiles.git $HOME/.dotfiles
$ dotfiles config --local status.showUntrackedFiles no
$ dotfiles checkout

# Probably some files are going to exist, so you may want to backup them and then retry checkout.
```

> NOTE: Before reloading my configuration as is. Make sure to install the necessary tools for the config to work.\
> These are detailed in the following sections.

# Building the Basic Environment
In this section I'm going to details the tools I use in my Arch environment. \
Some may be previously installed if you bared cloned this repository.

## Wallpapers

To setup wallpapers, install [swww](https://github.com/LGFae/swww).
```bash
$ sudo pacman -S swww
```
> swww config is done on the Hyprland config file. You can also use \
> swww {path} to set a wallpaper.

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
I use `EasyEffects`. I've also included some presets in the `extra-config` folder. \
To apply the presets, move them to `~/.config/easyeffects/output` and select them in the EasyEffects GUI.

For equalizer effects to work, install these plugins:
- calf
- lsp-plugins

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

## Monitor Setup
Refer to Hyprland's [Monitor Setup](https://wiki.hyprland.org/Configuring/Monitors)

## Trackpad Gestures
Refer to Hyprland [Touchpad Settings](https://wiki.hyprland.org/Configuring/Variables/#touchpad)

## Session Locker

I use [hyprlock](https://github.com/hyprwm/hyprlock) to lock the session.

My configuration automatically invokes hyprlock when returning from a suspend.

```bash
sudo pacman -S hyprlock
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
A list of software that I use in my environment, but that is not necessary for the configuration to work, or no detailed explanation for setup is needed.


| Software                     | Description                                    |
|------------------------------|------------------------------------------------|
| Dolphin                      | File Manager                                   |
| Less                         | Pager for Git and Arch journal                 |
| visual-studio-code-bin (AUR) | Propietary VsCode (for extension sync support) |
| spotify (AUR)                | ¯\_(ツ)_/¯                                     |
| Discord                      | Chat                                           |
| Gedit                        | Simple graphical text editor                   |
| obs-studio                   | Screen recording                               |
| galculator                   | Calculator                                     |
| filelight                    | Disk usage analyzer                            |
| bluez                        | Bluetooth stack                                |
| blueman                      | Bluetooth manager                              |
| htop                         | System monitor                                 |
