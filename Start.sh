#!/bin/bash
# Author: Diego Corradi
# simple service to start the bot
/usr/bin/python3 /home/pi/Adafruit_Python_DHT/examples/simple_bot_DHT.py

sudo service simple_bot_DHT.py start