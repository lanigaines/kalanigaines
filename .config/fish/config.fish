
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /Applications/anaconda3/bin/conda
    eval /Applications/anaconda3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/Applications/anaconda3/etc/fish/conf.d/conda.fish"
        . "/Applications/anaconda3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/Applications/anaconda3/bin" $PATH
    end
end
# <<< conda initialize <<<

