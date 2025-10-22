# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="gnzh"

# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-shift-select zsh-autosuggestions zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh

# User configuration


# You may need to manually set your language environment
autoload -Uz compinit && compinit
export LANG=en_US.UTF-8
export EDITOR='nvim'
export GSK_RENDERER=gl
alias ls='ls --color=auto'
alias grep='grep --color=auto'
neofetch --colors 1 5 1 1 7
alias hhdr='python ~/.config/hypr/scripts/hdr.py'

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
