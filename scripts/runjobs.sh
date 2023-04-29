#!/usr/bin/env bash
set -x

#/home/tw/.local/share/virtualenvs/data_wb-wSU96PeT/bin/python /home/tw/dev/opt/pyo-sched-machine/2/main.py random 3 3 --save

VIRTUAL="$HOME/.local/share/virtualenvs/data_wb-wSU96PeT"
WDIR="$HOME/dev/opt/pyo-sched-machine/2"

$VIRTUAL/bin/python $WDIR/main.py random 3 3 --save
