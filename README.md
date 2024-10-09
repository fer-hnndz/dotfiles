# Dotfiles

This is a collection of configuration files for my Arch installation.


# Table of Contents
1. [Pre-Installation](#Pre-Installation)
2. [Post Arch Installation](#Post-Arch-Installation)
3. [QTile and Login](#QTile-and-Login)
4. [Building the Basic Environment](#Building-the-Basic-Environment)
    1. [Wallpapers](#Wallpapers)
    2. [Audio](#Audio)
        - [Equalizer](#Equalizer)
    3. [Brightness and Redshift](#Brightness-and-Redshift)
    4. [Monitor Setup](#Monitor-Setup)
    5. [Trackpad Gestures](#Trackpad-Gestures)
    6. [GPU Drivers](#GPU-Drivers)
    7. [Fixing Suspend (sleep) issues](#Fixing-Suspend-(sleep)-issues)
        - [Suspend on Lid Close](#Suspend-on-Lid-Close)
        - [Turn off monitor after idle](#Turn-off-monitor-after-idle)
        - [Suspend after Idle](#Suspend-after-Idle)
    8. [Session Locker](#Session-Locker)
    9. [Battery Alerts](#Battery-Alerts)
    10. [Boot Screen](#Boot-Screen)
5. [Extra Tools](#Extra-Tools)
    1. [Program Launcher](#Program-Launcher)
    2. [AUR Helper (yay)](#AUR-Helper-(yay))
    3. [Applets](#Applets)
    4. [Notification Support](#Notification-Support)
    5. [OhMyZsh](#OhMyZsh)
6. [Extra Software](#Extra-Software)



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

For the bootloader I chose `rEFInd` since it was a less pain in the ass experience that GRUB.\
Refer to [rEFInd Installation](https://wiki.archlinux.org/title/REFInd).

```bash
# Point to the Arch root partition
refind-install --usedefault /dev/sdX
```
>Note for myself: When I first installed rEFInd, I had an issue where the rEFInd installation script will attempt to mount the live USB, resulting that whenever I tried to run without the USB, Arch won't boot.*

# QTile and Login

My to-go Window Manager is QTile. Simple enough for me.\
It may happen that some fonts are not displayed correctly, to fix this try to install some fonts:

```bash
$ sudo pacman -S ttf-dejavu ttf-liberation noto-fonts noto-fonts-cjk
```

Before running my custom config in QTile, install the mononoki nerd font that my config uses for icons.

```bash
$ sudo pacman -S firefox unzip

# After downloading Mononoki
$ unzip Mononoki.zip -d Mononoki
$ mkdir ~/.local/share/fonts/ttf
$ cp Mononoki ~/.local/share/fonts/ttf
```

To install all the useful stuff to setup QTile we need a LightDM, a greeter, a text editor (in case not installed) and `xterm` since that is what QTile will use by default.

```bash
$ sudo pacman -S lightdm lightdm-gtk-greeter qtile xterm firefox picom
$ sudo systemctl enable lightdm

# You may want to reboot so ligthdm launches QTile on the next boot.
$ systemctl reboot
```

## Setting up `dotfiles`

Once rebooted with the LightDM greeter, login into your user and you should see QTile.
Open a terminal and with a text editor edit your `.bashrc` file.

```bash
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

Once you have added the alias, clone the dotfiles repository.

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

For the wallpapers I prefer using [nitrogen](https://wiki.archlinux.org/title/Nitrogen).
```bash
$ sudo pacman -S nitrogen
$ nitrogen /path/to/wallpapers/dir
# Will open a window that allows you to pick a wallpaper even for different screens.

# To restore the last used wallpapers simply run
$ nitrogen --restore &
```

## Audio
I use [Pipewire](https://wiki.archlinux.org/title/PipeWire) for audio.
Refer to the installation guide for setup details.

```bash
$ sudo pacman -S pipewire pipewire-audio pipewire-pulse pipewire-alsa pipewire-jack
```
> **Install volumeicon and add it to your .xprofile to have a volume icon in the tray.**

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

## Brightness and Redshift

To control the brightness of the screen, you can use `brightnessctl`.\
You can also install [redshift](https://wiki.archlinux.org/title/Redshift) to control the color temperature of your screen.

```bash
$ sudo pacman -S brightnessctl redshift
$ redshift -l LAT:LON
```

## Monitor Setup
`xrandr` allows for CLI support to edit monitor orientation.
My QTile config automatically setups the monitor positions based on how I currently use my laptop and monitor.

```bash
# Install tools
sudo pacman -S xorg-xrandr arandr
```

If you ever want to change the monitor orientation, use `arandr` and copy the script for `xrandr`, then paste it on the `screens.py` file accordingly on `~/.config/qtile/`.

## Trackpad Gestures
To allow gestures like scrolling and tapping, you can install [xf86-input-synaptics](https://wiki.archlinux.org/title/Touchpad_Synaptics).

```bash
sudo pacman -S xf86-input-synaptics
```
Refer to the wiki to setup the gestures, or copy the `70-synaptics.conf` file located in `extra-config` to `/etc/X11/xorg.conf.d/`.

## GPU Drivers
You may want to install GPU drivers, just in case.\
For my specific machine, I had to install AMD Drivers.

```bash
$ sudo pacman -S xf86-video-amdgpu mesa vulkan-radeon
```

## Fixing Suspend (sleep) issues

### Suspend on Lid Close
To enable suspend on lid close, install acpid and enable the service.

```bash
$ sudo pacman -S acpid
$ sudo systemctl enable acpid
$ sudo systemctl start acpid
```

Then, copy the file `logind.conf` located in `extra-config` to `/etc/systemd/`. And restart the service.

```bash
$ sudo cp logind.conf /etc/systemd/
$ sudo systemctl restart systemd-logind
```

### Turn off monitor after idle

I like to turn off the monitors without suspending the system after idling.\
There's a section about [Display Power Management Signaling (DPMS) specially for Xorg](https://wiki.archlinux.org/title/Display_Power_Management_Signaling#Xorg).

To apply the settings, copy the file `10-serverflags.conf` located in `extra-config` to `/etc/X11/xorg.conf.d/10-serverflags.conf`.

### Suspend after Idle

I use `xautolock` to suspend the system after a certain amount of time.

```bash
$ sudo pacman -S xautolock
```

Then, in my `.xprofile` I start the service.

```bash
...
# Set bottom right corner as a position where system won't sleep
xautolock -time 5 -locker "~/xautolock-suspend.sh" -corners 000- &
...
```

## Session Locker

I use [slock](https://wiki.archlinux.org/title/Slock) to lock the session.

I also set up a service to suspend the system after a certain amount of time.

Copy `slock@.service` located in `extra-config` to `/etc/systemd/system/`.
Then, enable the service.
```bash
$ sudo systemctl enable slock@user.service`
$ sudo systemctl start slock@user.service`
```

> NOTE: Replace user with your username.
## Battery Alerts

To add alerts when battery is low I use [battery-advisor](https://github.com/fer-hnndz/battery-advisor) \
And by the way, I created this package :).

```bash
yay -S battery-advisor
```

Then, in my `.xprofile` I start the service.

```bash
...
battery-advisor &
...
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

Then in my `.xprofile` I start the applets.

```bash
...
nm-applet &
...
```

## Notification Support

First, install the required dependencies for notifications. \
Then, copy the file called `org.freedesktop.Notifications.service` located in `extra-config` to `/usr/share/dbus-1/services`

Or do it manually like so:
```bash
$ sudo pacman -S libnotify notification-daemon
$ sudo nano /usr/share/dbus-1/services/org.freedesktop.Notifications.service

# Paste these lines
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon

# To try the notification service
$ notify-send "Hello World!"
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
| Flameshot                    | Screenshot tool                                |

