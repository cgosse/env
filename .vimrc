"let $PYTHONHOME = "/anaconda"
"let $PYTHONPATH = $PYTHONHOME . "/Lib"
"let $PATH = $PATH . ';' . $PYTHONHOME

execute pathogen#infect()
" unknown why this one doesn't work, some suggest set nocp before infecting
" execute pathogen#helptagso()

" try to fix slow python mode
let g:pymode_rope_lookup_project = 0

" yank to the system clipboard by default
set clipboard+=unnamed

" syntax on
" filetype on
" these are for the vim-R plugin
syntax enable
filetype plugin on
au BufNewFile,BufRead *.cl set filetype=c
" set spellcheck for latex, text, and markdown files
au BufNewFile,BufRead *.tex set spell
au BufNewFile,BufRead *.txt set spell
au BufNewFile,BufRead *.md set spell
" syntax highlighting for gnuplot files
au BufNewFile,BufRead *.plt set filetype=gnuplot


" use :set gfn to find out what to put on this line
set guifont=Liberation\ Mono\ 11
"set guifont=Ubuntu\ Mono\ 10
"hi LineNr guifg=darkgreen
"hi LineNr guifg=gray guibg=darkgray
"hi LineNr guifg=darkgreen
"hi LineNr ctermfg=gray ctermbg=darkgray

" this uses the right colors if you've set your terminal to solarized
colorscheme solarized
if has('gui_running')
"  "set background=light
  set lines=30 columns=87
else
	" if you use Xresources to set colors, pick 16 here instead of 256
	let g:solarized_termcolors=16
"  set background=dark
	set t_Co=16
endif

set nonumber

" automatically use the working directory of the file being edited
"set autochdir

filetype indent on
set cindent
" smartindent is no longer perferred per stack exchange
" set smartindent
set autoindent
" autowrite allows you to switch buffers without saving each manually first
set autowrite
" set auto-indenting on for programming
set ai
" prefer 2 space actual tabs
"set tabstop=2 softtabstop=0 noexpandtab shiftwidth=2
" use spaces instead of tab characters
set tabstop=4 softtabstop=4 expandtab shiftwidth=4 smarttab

" turn off compatibility with the old vi
set nocompatible

" turn on the "visual bell" - which is much quieter than the "audio blink"
set vb

" highlight words when searching for them.
set hlsearch

" automatically show matching brackets. works like it does in bbedit.
set showmatch

" do NOT put a carriage return at the end of the last line! if you are programming
" for the web the default will cause http headers to be sent. that's bad.
set binary noeol

" make that backspace key work the way it should
set backspace=indent,eol,start

set ignorecase

set formatoptions=l
set lbr
set wrap

" use F9 to toggle folds
inoremap <F9> <C-O>za
nnoremap <F9> za
onoremap <F9> <C-C>za
vnoremap <F9> zf

" use two z's to exit insert mode to avoid having to hit esc
:imap zz <Esc>

" make arrow keys work within tmux
if &term =~ '^screen'
    " tmux will send xterm-style keys when its xterm-keys option is on
    execute "set <xUp>=\e[1;*A"
    execute "set <xDown>=\e[1;*B"
    execute "set <xRight>=\e[1;*C"
    execute "set <xLeft>=\e[1;*D"
endif

" always use rainbow color parens and friends
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces

