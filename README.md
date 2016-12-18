# raspberrypi-serial
Reads data from serial ports using python and updates database

Make sure your arduino device is on serial speed 115200 and check the device mine is /dev/ttyACM0
hint: You can unplug the arduino then plug it in and run dmesg to see details on which serial port it's on.

Example json used from an arduino device

{"sender": 2,"strength": -83}
{"nodeId": 2,"itemLocation": 1,"trigger": 1}

