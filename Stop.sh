#!/bin/bash
# Author: Diego Corradi
# simple service to stop the bot
for KILLPID in `ps ax | grep ‘simple_bot_DHT.py’ | awk ‘{print $1;}’`; do
kill -9 $KILLPID;
done
