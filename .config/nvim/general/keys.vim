" Remape escape (ESC)

nnoremap <C-c> <Esc>
inoremap jk <Esc>

" Use alt + hjkl to reisize window

nnoremap <M-j> :resize -2<CR>
nnoremap <M-k> :resize +2<CR>
nnoremap <M-h> :vertical resize -2<CR>
nnoremap <M-l> :vertical resize +2<CR>

" Alternative way to save

nnoremap <C-s> :w<CR>

" Alternative way to quit and save 

nnoremap <C-x> :wq!<CR>
nnoremap <C-q> :q!<CR>
" Tab in normal mode will move to next buffer

nnoremap <M-TAB> :bnext<CR>
"SHIFT+TAB in normal mode move to previous buffer

nnoremap <S-TAB> :bprevious<CR>

" Close current buffer

nnoremap <C-b> :bd<CR>

" Tab on nnoremap
nnoremap <TAB> <gv

" Better tabbing mode

vnoremap < <gv
vnoremap > >gv

" Move selected line or block of text in visual mode
" shift + k to move up
" shift + j to move downx

xnoremap K :move '<-2<CR>gv-gv
xnoremap J :move '>+1<CR>gv-gv


"Better window navigation

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l


