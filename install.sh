#!/bin/bash
# Fer's dotfiles installation script
set -euo pipefail

echo "[INFO] Starting dotfiles installation..."
sudo pacman -Syu --noconfirm

# -------------------------
# 2️⃣ Instalar paquetes de pacman
# -------------------------
PACMAN_PKGS= (
    alsa-utils
    arch-install-scripts
    brightnessctl
    btop
    btrfs-progs
    calf
    cliphist
    cmatrix
    dhcpcd
    discord
    docker
    docker-compose
    dotnet-runtime
    duf
    easyeffects
    evince
    ffmpeg-audio-thumbnailer
    ffmpegthumbnailer
    filelight
    firefox
    gedit
    git
    gnome-calculator
    gparted
    hypridle
    hyprland
    hyprlock
    hyprpolkitagent
    hyprshot
    hyprutils
    imagemagick
    jdk21-openjdk
    kitty
    less
    loupe
    lsp-plugins
    man-db
    nautilus
    neovim
    network-manager-applet
    networkmanager
    nodejs
    noto-fonts
    noto-fonts-cjk
    noto-fonts-emoji
    npm
    ntfs-3g
    ntp
    obs-studio
    pacman-contrib
    pamixer
    papirus-icon-theme
    pavucontrol
    pipewire-alsa
    plymouth
    postgresql
    python-pillow
    python-uv
    qt5-graphicaleffects
    qt5-quickcontrols2
    qt5-wayland
    refind
    reflector
    rofi
    stow
    sublime-text-4
    swaync
    swayosd-git
    swww
    ttf-dejavu
    ttf-liberation
    ttf-segoe-ui-variable
    vlc
    vlc-plugin-ffmpeg
    vlc-plugin-gstreamer
    vulkan-radeon
    waybar
    wl-clipboard
    wlsunset
    woff2-font-awesome
    xdg-desktop-portal-hyprland
    yarn
    yay
    zapzap
    zsh
)

AUR_PACKAGES = (
    zapzap
    visual-studio-code-bin
    spotify
    sublime-text-4
    swayosd-git
    apple-fonts
)

echo "[INFO] Installing pacman packages..."
sudo pacman -S --needed --noconfirm "${PACMAN_PKGS[@]}"

echo "[INFO] Installing AUR packages..."
paru -S --noconfirm --needed "${AUR_PACKAGES[@]}"

DOTFILES_DIR="$HOME/dotfiles"
if [ ! -d "$DOTFILES_DIR" ]; then
    echo "[INFO] Cloning dotfiles..."
    git clone git@github.com:fer-hnndz/dotfiles.git "$DOTFILES_DIR"
fi

cd "$DOTFILES_DIR"

# Aplicar módulos stow
echo "[INFO] Aplicando dotfiles..."
stow --adopt zsh nvim kitty hypr-laptop easyeffects rofi waybar fontconfig neofetch


SERVICES=(
    NetworkManager
    ntpd
    sshd
)

echo "[INFO] Habilitando servicios..."
for svc in "${SERVICES[@]}"; do
    sudo systemctl enable --now "$svc"
done

echo "[OK] Instalación completa!"
