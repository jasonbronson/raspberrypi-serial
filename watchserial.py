#!/usr/bin/python

import serial, time, json, MyMqtt, MyEnv
#initialization and open the port

#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 1            #non-block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

try: 
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():

    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output 
                 #and discard all that is in buffer

        numOfLines = 0
       
	while True:
          response = ser.readline()
	  sender = ''
	  strength = ''
	  nodeId = ''
          itemLocatin = ''
	  trigger = ''
	  if response:
            try:
		print("reading serial data: " + response)
	    	lineData = json.loads(response)
		
		if 'sender' in lineData:
		 sender = lineData['sender']
	         strength = lineData['strength']
		
		if 'nodeId' in lineData:
		 nodeId = lineData['nodeId']
		 itemLocation = lineData['itemLocation']
		 trigger = lineData['trigger']
		 
	    except Exception, ValueError:
		print("JSON Decoding has failed")
          numOfLines = numOfLines + 1


        ser.close()
    except Exception, e1:
        print "error communicating...: " + str(e1)

else:
    print "cannot open serial port "
