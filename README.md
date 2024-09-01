# Dotfiles

This is a collection of configuration files for my Arch installation.

Special thanks to [@AntonioSarosi](https://github.com/antoniosarosi/dotfiles) who I reffered from to make my own QTile configuration and other program choices.

# Table of Contents
1. [Post Arch Installation](#post-arch-installation)
2. [Qtile and Login](#qtile-and-login)
   - [Setting up `dotfiles`](#setting-up-dotfiles)
3. [Building the Basic Environment](#building-the-basic-environment)
   - [Wallpapers](#wallpapers)
   - [Audio](#audio)
   - [Brightness and Redshift](#brightness-and-redshift)
   - [Monitor Setup](#monitor-setup)
   - [Trackpad Gestures](#trackpad-gestures)
   - [GPU Drivers](#gpu-drivers)
4. [Extra Tools](#extra-tools)
   - [Program Launcher](#program-launcher)
   - [AUR Helper (yay)](#aur-helper-yay)
   - [Applets](#applets)
   - [Notification Support](#notification-support)
   - [OhMyZsh](#ohmyzsh)
5. [Extra Software](#extra-software)

# Post Arch Installation
After installing Arch on the live USB make sure you have installed some utilites for later.

```bash
$ pacman -S networkmanager nano sudo git
$ systemctl enable networkmanager.service

# Make sure to setup correctly the sudoers file and add the your user to it.

# Use nano (my preffered console text editor) to edit the sudoers file.
$ export EDITOR=nano;
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
$ sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
```

Before installing QTile, since my configuration uses a Nerd Font (mononoki), install that too.

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
$ git clone --bare https://github.com/fer-hnndz/dotfiles.git $HOME/.dotfiles
$ dotfiles config --local status.showUntrackedFiles no
$ dotfiles checkout

# Probably some files are going to exist, so you may want to backup them and then retry checkout.
```
> NOTE: Before reloading QTile with my configuration, make sure to install necessary programs.
> ```bash
>$ sudo pacman -S zsh alacritty rofi xorg-xrandr arandr xf86-input-synaptics
>```

# Building the Basic Environment
In this section I'm going to details the tools I use in my Arch environment. \
Some may be previously installed if you bared cloned this repository.

## Wallpapers

For the wallpapers I prefer using `nitrogen`.
```bash
$ sudo pacman -S nitrogen
$ nitrogen /path/to/wallpapers/dir
# Will open a window that allows you to pick a wallpaper even for different screens.

# To restore the last used wallpapers simply run
$ nitrogen --restore &
```

## Audio
Imagine using Arch with no audio. Impossible. Get some audio:

```
sudo pacman -S pulseaudio pavucontrol pamixer
```

`pulseaudio` will allow for audio support while `pavucontrol` and `pamixer` offer a GUI and CLI setup respectively. \
Installing and rebooting should be enough to get audio working. Although you may have some issues.

## Brightness and Redshift

You may be using a laptop, so to take care of your eyes, you may want to control the brightness of your screen.
You can also install [redshift](https://wiki.archlinux.org/title/Redshift) to control the color temperature of your screen.

```bash
$ sudo pacman -S brightnessctl redshift
$ redshift -l LAT:LON
```

## Monitor Setup
`xrandr` allows for CLI support to edit monitor orientation.
My QTile config automatically setups the monitor positions based on how I currently use my laptop and monitor. \
To install both tools:

```bash
sudo pacman -S xorg-xrandr arandr
```

If you ever want to change the monitor orientation, use `arandr` and copy the script for `xrandr`.

## Trackpad Gestures
To allow gestures like scrolling and tapping, you can install [xf86-input-synaptics](https://wiki.archlinux.org/title/Touchpad_Synaptics).

```bash
sudo pacman -S xf86-input-synaptics
```

## GPU Drivers
You may want to install GPU drivers, just in case.\
For my specific machine, I had to install AMD Drivers.

```bash
$ sudo pacman -S xf86-video-amdgpu mesa
```

# Extra Tools
In this section I'm going to detail some extra tools that I use in my Arch environment that speed up my workflow.

## Program Launcher
[Rofi](https://wiki.archlinux.org/title/Rofi) is a program launcher just like MacOS's Spotlight.\
You can install it with:

```bash
$ sudo pacman -S rofi
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
I use only really need 2 applets, one for the volume and other for the network.

```bash
$ sudo pacman -S network-manager-applet volumeicon
```

Then in my `.xprofile` I start the applets.

```bash
...
volumeicon &
nm-applet &
...
```

## Notification Support

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

| Less                         | Pager for Git and Arch journal                 |
|------------------------------|------------------------------------------------|
| visual-studio-code-bin (AUR) | Propietary VsCode (for extension sync support) |
| spotify-launcher             | ¯\_(ツ)_/¯                                     |











