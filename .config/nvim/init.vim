" General

source $HOME/.config/nvim/general/settings.vim
source $HOME/.config/nvim/general/keys.vim

" Pluggins

source $HOME/.config/nvim/vim-plug/plugins.vim
source $HOME/.config/nvim/pack/kite/start/vim-plugin/autoload/kite.vim " For this is necesary run :PlugInstall

" Themes

source $HOME/.config/nvim/general/colors.vim
" source $HOME/.config/nvim/themes/ayu.vim
colorscheme OceanicNext
source $HOME/.config/nvim/themes/airline.vim

" Plug configuration 

source $HOME/.config/nvim/confscripts/easymotion.vim
source $HOME/.config/nvim/confscripts/nerdtree.vim
source $HOME/.config/nvim/confscripts/rainbow.vim
source $HOME/.config/nvim/confscripts/kite.vim
source $HOME/.config/nvim/confscripts/git.vim
source $HOME/.config/nvim/confscripts/fzf.vim

" Syntax highlight configuration

source $HOME/.config/nvim/syntax/syntax.vim
source $HOME/.config/nvim/syntax/gas.vim
source $HOME/.config/nvim/syntax/mysyntax.vim
