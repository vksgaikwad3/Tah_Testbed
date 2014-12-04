# This script will upload the Arduino test sketches to Tah and test for Analog LOW-HIGH and Digital LOW-HIGH states

import RPi.GPIO as GPIO
import os
import time
import RpiInit
import xlwt
from datetime import datetime
from Tah_Testing import Tah 
from lcd_1 import HD44780


#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(22, GPIO.OUT, pull_up_down=GPIO.PUD_UP)

prev_state = 0
testbed = Tah()
lcd = HD44780()

lcd.__init__()
lcd.clear()
lcd.message('starting')

book = xlwt.Workbook(encoding="utf-8") 
sheet1 = book.add_sheet("Tah First Batch ") 

sheet1.write(2,0, 'Sr.No')
sheet1.write(2,1,"Start Time")
sheet1.write(2,2,"End Time")
sheet1.write(2,3,"Elapsed Time")
sheet1.write(2,4,"Remark")

row =5
col =0
count =0
val =0
i=0
while (val<2):
	RpiInit.init()		#initialze all GPIOs

	val =val+1
	# Switch input 
	startTest = GPIO.input(11)		#Read Start pulse from Switch S1
	print startTest
	if((not prev_state) and startTest):	#switch press
		GPIO.output(23,GPIO.HIGH)		#Buzzer ON
		time.sleep(0.5)
		GPIO.output(23,GPIO.LOW)		# OFF Buzzer
	        
		#Test  Start Time Log
		lcd.__init__()
		'''lcd.message("Bootloader \n Burning...")
		
		os.chdir("/home/pi/GitRepo/Tah_Testbed/bootloaders/")
		time.sleep(1)
		os.system("./atm32U4.sh")
		GPIO.output(22,GPIO.LOW)
		'''
		StartTime  = datetime.now()
		lcd.message("Analog LOW Test") 
		#Testing Started here
		os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogLow/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		AL = testbed.testAnalogLow()
                print AL 	
	
# Now test for Analog HIGH states
		lcd.__init__()
		lcd.message('Analog HIGH Test')

                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogHigh/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
                AH = testbed.testAnalogHigh()
		print AH

# NOw test for Digital LOW  State
		lcd.__init__()
		lcd.message('GPIO LOW Test')

                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOLow/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		DL = testbed.testGPIOLow()
		print DL

#Now test for Digital HIGH state
		lcd.__init__()
		lcd.message('GPIO HIGH Test')

                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOHigh/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		DH = testbed.testGPIOHigh()
	
		print DH
		print "Done Testing"

		
		
		sheet1.write(row,0,str(count))
		sheet1.write(row,1,str(StartTime))
	

		row = row+1 
		count = count+1
		
		if(AL ==6 and AH ==6 and DL==12 and DH ==12):

			os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/ArdSCL/")	# Upload ArdSCL sketche
   		        os.system("make")
                	os.system("make upload")
			
			EndTime  = datetime.now()	
				
			ElapsedTime = EndTime - StartTime
			print "ElapsedTime:",ElapsedTime

			sheet1.write(row,2,str(EndTime))
			sheet1.write(row,3,str(ElapsedTime))
			
                	sheet1.write(row,4,"PASS")
			print 'PASS'

			GPIO.output(23,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(23,GPIO.LOW)
               	 	
			lcd.__init__()
			lcd.message('Tested OK!')
			
		else:
			sheet1.write(row,2,str(EndTime))
                        sheet1.write(row,3,str(ElapsedTime))

                	sheet1.write(row,4,"Failed")
			print 'Failed'
			lcd.__init__()
			lcd.message('Failed')
			
			while(i<2):			
				GPIO.output(23,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(23,GPIO.LOW)
				i=i+1

		book.save("Tah_TestbeReport.xls")
	else:
		print 'Lets Start Test '
