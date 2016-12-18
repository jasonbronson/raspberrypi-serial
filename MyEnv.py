#!/usr/bin/python

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Mqtt settings
MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = os.environ.get("MQTT_PORT")

#serial port settings
SERIAL_PORT = os.environ.get("SERIAL_PORT")
BAUD_RATE = os.environ.get("BAUD_RATE")

