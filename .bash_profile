#!/bin/zsh
setxkbmap -layout us,us -variant ,intl -option 'grp:alt_shift_toggle' &
volumeicon &
nm-applet &
picom --fade-in-step=1 --fade-out-step=1 --fade-delta=0 &
nitrogen --restore &