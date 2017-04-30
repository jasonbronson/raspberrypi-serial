#!/usr/bin/python

import logging, serial, time, json, MyMqtt, MyEnv
#initialization and open the port

#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()
ser.port = MyEnv.SERIAL_PORT
ser.baudrate = MyEnv.BAUD_RATE
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 1            #non-block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

try: 

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("/tmp/serialwatcher.log")
    logger.addHandler(fh)
    
    ser.open()
except Exception, e:
    logger.debug( "error open serial port: " + str(e))
    exit()

if ser.isOpen():

    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output 
                 #and discard all that is in buffer

        numOfLines = 0

        sender = ''
        strength = ''
        nodeId = ''
        itemLocatin = ''
        trigger = ''

        while True:
              response = ser.readline()

              if response:
                    try:
                        logger.debug("DEBUG - reading serial data: " + response)
                        lineData = json.loads(response)

                        if 'senderId' in lineData:
                          senderId = lineData['senderId']
                          trigger = lineData['trigger']
                          lineData['time'] = time.strftime("%H:%M:%S")
                          lineData['date'] = time.strftime("%d/%m/%Y")
                          strength = lineData['strength']
                          #MyMqtt.publishMessage(senderId, json.dumps(lineData))
                          MyMqtt.publishMessage(senderId, trigger)

                    except Exception, ValueError:
                      logger.debug("JSON Decoding has failed: " + str(ValueError) )

                    numOfLines = numOfLines + 1


        ser.close()
    except Exception, e1:
        logger.debug("error communicating...: " + str(e1))

else:
    logger.debug("cannot open serial port")
