"""shiftRegister.py - Scott K 11/6/12
   Shift Register object for use with beagle bone
"""

#-----------------------------------------------------------------------------

from bbio import *

class shiftRegister(object):

def _init_(self, ser=8, rclk=9, srclk=10, numReg=1):
    self.SER = ser	    				   	  #pin 14 on the 75HC595
    self.RCLK = rclk    				 	  #pin 12 on the 75HC595
    self.SRCLK = srclk  				 	  #pin 11 on the 75HC595
    
    self.NUM_REGISTERS=numReg   				  #number of shift registers
    self.NUM_REG_PINS=NUM_REGISTERS*8                      #number of total pins

    self.registers[NUM_REG_PINS]



def configure():
	"""Sets all of the control pins to output and then makes them all LOW"""
    pinMode(self.SER, OUTPUT)
    pinMode(self.RCLK, OUTPUT)
    pinMode(self.SRCLK, OUTPUT)

    #reset all register pins
    clearRegisters()
    writeRegisters()
  
#-----------------------------------------------------------------------------          

def clearRegisters():
	"""Makes shift register pins go LOW"""
    for(int i = NUM_REG_PINS - 1; i >=  0; i--):
         self.registers[i] = LOW

#-----------------------------------------------------------------------------

def writeRegisters():
	"""Writes values to all shift register pins after they have been set"""
    digitalWrite(self.RCLK, LOW)
  
    for i in range(self.NUM_REG_PINS):
        digitalWrite(self.SRCLK, LOW)
        int val = registers[self.NUM_REG_PINS-1-i]
        digitalWrite(self.SER, val)
        digitalWrite(self.SRCLK, HIGH)
    
    digitalWrite(self.RCLK, HIGH)

#-----------------------------------------------------------------------------

def setRegisterPin(int index, int value):
	"""Sets, but does not right the value of a shift register pin"""
    self.registers[index] = value

#-----------------------------------------------------------------------------

def setPins(pins[], value[]):
	"""Sets an array of pin numbers to a corresponding value according to a seperate an array"""
	for i in range(pins):			#cycles through pin numbers
		newVal=LOW
		if value[i]:
			newVal=HIGH
		setRegisterPin(pins[i], newVal)  #sets pin to the value at a corresponding value of the second array
	writeRegisters()  					#physically changes pin values