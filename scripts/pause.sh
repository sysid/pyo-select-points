#!/usr/bin/env bash

PID=4177

start () {
    echo "-M- continuing process: $PID"
    kill -CONT $PID
}

stop () {
    echo "-M- pausing process: $PID"
    kill -SIGSTOP $PID
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
        echo $"Usage:  {start|stop}"
        exit 1
esac

