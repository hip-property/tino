#!/usr/bin/env bash

rm /usr/local/bin/tino_util 2> /dev/null
rm /usr/local/bin/tino 2> /dev/null
ln -s $(pwd)/tino_util.py /usr/local/bin/tino_util
ln -s $(pwd)/tino.py /usr/local/bin/tino

echo "To add command auto completion please add the following to ~/.zshrc"
echo "fpath=($(pwd)/completion \$fpath)"
