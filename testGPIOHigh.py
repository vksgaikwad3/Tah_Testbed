import RPi.GPIO as GPIO
import time
import os
import RpiInit
from lcd_1 import HD44780
import serial


RpiInit.init()
lcd =  HD44780()

# setup input channel
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(21,GPIO.IN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(21, GPIO.LOW)
while True:

        GPIO.setwarnings(False)
        #value =GPIO.input(21)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)       # set channel 11 
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
       #lcd.message("A0 Testing")
        print "D2 Testing"
        #GPIO.cleanup(21)
        value0 =GPIO.input(21)          # Mux output pin
        print value0
	if value0:
                print "D2 OK"
        else:
                print "D2 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)
                           
	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 10
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)

        print "D3 Testing"
        value1 = GPIO.input(21)         # read input
        print value1
	if value1:
                print "D3 OK"
        else:
                print "D3 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

	GPIO.output(15,GPIO.HIGH)
        GPIO.output(19,GPIO.LOW)        # set channel 9
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        print "D4 Testing"
        value2 = GPIO.input(21)         # read input
        if value2:
                print "D4 OK"
        else:
                print "D4 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)        # set channel 8
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        print "D5 Testing"
        value3 = GPIO.input(21)         # read input
        if value3:
                print "D5 OK"
        else:
                print "D5 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(15,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)        # set channel 7
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D6 Testing"
        value4 = GPIO.input(21)         # read input
        if value4:
                print "D6 OK"
        else:
                print "D6 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D7 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "D7 OK"
        else:
                print "D7 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)


	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D8 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "D8 OK"
        else:
                print "D8 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D9 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "D9 OK"
        else:
                print "D9 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D10 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "D10 OK"
        else:
                print "D10 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D11 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "D11 OK"
        else:
                print "D11 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)


	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D12 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "D12 OK"
        else:
                print "D12 Failed"
        #GPIO.setup(21,GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "D13 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "D13 OK"
        else:
                print "D13 Failed"
        #GPIO.setup(21,GPIO.LOW)

	time.sleep(0.5)
        break


print "GPIO Tested"
GPIO.cleanup()





