# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="intheloop"

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
export TERM=xterm-256color
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"

export PATH=$PATH:~/.dotnet/tools
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
export PATH="$HOME/.npm-global/bin:$PATH"

. /usr/share/nvm/init-nvm.sh
fastfetch
