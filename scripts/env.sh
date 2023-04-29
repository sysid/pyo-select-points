#!/usr/bin/env bash

Cyan "-M- sourcing $BASH_SOURCE"

echo "-M- Creating alias: /home/tw/.local/share/virtualenvs/data_wb-wSU96PeT/bin/python"
alias python=/home/tw/.local/share/virtualenvs/data_wb-wSU96PeT/bin/python

echo "-M- Creating alias: show-logdata"
alias show-logdata='echo "select * from logdata"|sqlite3 logdata.db'

echo "-M- Creating alias: ipython"
alias ipython=/home/tw/.local/share/virtualenvs/data_wb-wSU96PeT/bin/ipython -i $PROJ_DIR/script/ipy.py
