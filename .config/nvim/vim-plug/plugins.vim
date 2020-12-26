call plug#begin('~/.config/nvim/plugged')

	" Syntax support

	Plug 'sheerun/vim-polyglot'
	
	"Rainbow brackets

	Plug 'frazrepo/vim-rainbow'
	
	" Kite Plug
	
	Plug 'kiteco/vim-plugin'
	
	" Easy Motion 
	
	Plug 'easymotion/vim-easymotion'

	" Autopairs

	Plug 'jiangmiao/auto-pairs'

	" File explorer

	Plug 'scrooloose/nerdtree'    
	
	" Icons

	Plug 'ryanoasis/vim-devicons'

	" Intellisense

	Plug 'neoclide/coc.nvim', {'branch': 'release'}

	" Airline

	Plug 'vim-airline/vim-airline'
	Plug 'vim-airline/vim-airline-themes'
	
	" Indent guides

	Plug 'Yggdroot/indentLine' 
	
	" Git integration

	Plug 'mhinz/vim-signify'
	Plug 'tpope/vim-fugitive'
	Plug 'tpope/vim-rhubarb'
	Plug 'junegunn/gv.vim'

	" Autoclose tags
	Plug 'alvan/vim-closetag'

	" Themes 
	Plug 'joshdick/onedark.vim'
	Plug 'kaicataldo/material.vim'
	Plug 'tomasiser/vim-code-dark'
	Plug 'crusoexia/vim-monokai'
	Plug 'ayu-theme/ayu-vim'
	Plug 'dracula/vim', { 'as': 'dracula' }

call plug#end()
