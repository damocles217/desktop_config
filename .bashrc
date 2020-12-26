#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

. ~/.git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1

neofetch

export PS1='\[\e[1;34m\][\[\e[m\]\[\e[1;33m\]\u\[\e[m\]\[\e[1;35m\]@\[\e[m\]\[\e[1;36m\]\h\[\e[m\]:\[\e[1;31m\]\W\[\e[m\]\[\e[1;34m\]]\[\e[m\]\[\033[33m\]$(__git_ps1 "(%s)")\[\033[37m\]\$ '