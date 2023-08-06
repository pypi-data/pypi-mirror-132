CONFIG_PATH=$HOME/.config/zsh/config.d

# Load the critical scripts.
source $CONFIG_PATH/init.zsh

FILES_STR=$(fd --glob '*.zsh' --exclude 'init.zsh' $CONFIG_PATH)
FILES=($(echo $FILES_STR | tr '\n' ' '))

# Load the partials.
for FILE in $FILES; do
    source $FILE
done
