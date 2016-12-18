#!/usr/bin/python

import paho.mqtt.publish as publish, MyEnv


def publishMessage(id, message):
  print(message)
  publish.single("alarm/" + str(id) , message, hostname=MyEnv.MQTT_HOST, port=MyEnv.MQTT_PORT)

