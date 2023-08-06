# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
# if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#   source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
# fi

# https://stackoverflow.com/questions/51006002/how-do-i-get-intellij-terminal-to-work-properly-with-oh-my-zsh
# https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003553899-Change-colors-for-Oh-my-zsh-in-PHPStorm-terminal
# system-wide environment settings for zsh(1)
if [ -x /usr/libexec/path_helper ]; then
	eval `/usr/libexec/path_helper -s`
fi

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# https://github.com/romkatv/powerlevel10k
# Main `p10k` configuration.
# Run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

ZSH_THEME="powerlevel10k/powerlevel10k"

# Plugins can be found in `~/.oh-my-zsh/plugins/*`.
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Add wisely, as too many plugins slow down shell startup.
plugins=(zsh-completions zsh-syntax-highlighting zsh-autosuggestions)
autoload -U compinit && compinit

source $ZSH/oh-my-zsh.sh
