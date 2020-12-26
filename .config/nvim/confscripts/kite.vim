let g:kite_supported_languages = ['*']
let g:kite_tab_complete = 1

set completeopt+=menuone
set completeopt+=noselect
let g:kite_previous_placeholder = '<C-H>'
let g:kite_next_placeholder = '<C-L>'
set statusline=%<%f\ %h%m%r%{kite#statusline()}%=%-14.(%l,%c%V%)\ %P
set laststatus=2  " always display the status line

autocmd FileType python let b:coc_suggest_disable = 1
autocmd FileType javascript let b:coc_suggest_disable = 1
autocmd FileType typescript let b:coc_suggest_disable = 1
autocmd FileType html let b:coc_suggest_disable = 1
autocmd FileType css let b:coc_suggest_disable = 1
"autocmd FileType c let b:coc_suggest_disable = 1
"autocmd FileType cpp let b:coc_suggest_disable = 1
autocmd FileType scss setl iskeyword+=@-@
autocmd FileType go let b:coc_suggest_disable = 1

if &filetype == "javascript" || &filetype == "python" || &filetype == "go" || &filetype == "html" || &filetype == "css" || &filetype == "typescript" || &filetype == "c"
	inoremap <C-space> <C-x><C-u>
elseif &filetype == "h" || &filetype == "cpp"
	inoremap <C-space> <C-x><C-u>
else
	inoremap <silent><expr> <c-space> coc#refresh()
endif
