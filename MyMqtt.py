#!/usr/bin/python

import requests, json, MyEnv

url = 'https://io.adafruit.com/api/feeds/'

def publishMessage(id, message):
  #print(message)
  if id == 2: #garage side door
    feedId=MyEnv.GARAGEDOOR_FEEDID
    data=json.loads('{  "value": "' + str(message) + '" }')

  if feedId:
    fullURL=url + str(feedId) + "/data?x-aio-key=" + MyEnv.API_KEY
    response = requests.post(fullURL, data=data)
    if response.status_code == 503:
      print("Throttled save")
    print(response)


  #publish.single("alarm/" + str(id) , message, hostname=MyEnv.MQTT_HOST, port=MyEnv.MQTT_PORT)

