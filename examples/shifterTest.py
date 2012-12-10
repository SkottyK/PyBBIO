# shift_test.py - Scott K 11/6/2012
# 
# Interfaces with shift registers to create displays.
# 
# This example is in the public domain
from bbio import *

SER = 8	    				   	  #pin 14 on the 75HC595
RCLK = 9     				 	  #pin 12 on the 75HC595
SRCLK = 10   				 	  #pin 11 on the 75HC595

NUM_REGISTERS=2   				  #number of shift registers
NUM_REG_PINS=NUM_REGISTERS*8                      #number of total pins

registers[NUM_REG_PINS]

#-----------------------------------------------------------------------------

def configure():
	"""Sets all of the control pins to output and then makes them all LOW"""
    pinMode(SER, OUTPUT)
    pinMode(RCLK, OUTPUT)
    pinMode(SRCLK, OUTPUT)

    #reset all register pins
    clearRegisters()
    writeRegisters()
  
#-----------------------------------------------------------------------------          

def clearRegisters():
	"""Makes shift register pins go LOW"""
    for(int i = NUM_REG_PINS - 1; i >=  0; i--):
         registers[i] = LOW

#-----------------------------------------------------------------------------

def writeRegisters():
	"""Writes values to all shift register pins after they have been set"""
    digitalWrite(RCLK, LOW)
  
    for i in range(NUM_REG_PINS):
        digitalWrite(SRCLK, LOW)
        int val = registers[NUM_REG_PINS-1-i]
        digitalWrite(SER, val)
        digitalWrite(SRCLK, HIGH)
    
    digitalWrite(RCLK, HIGH)

#-----------------------------------------------------------------------------

def setRegisterPin(int index, int value):
	"""Sets, but does not right the value of a shift register pin"""
    registers[index] = value

#-----------------------------------------------------------------------------

def setPins(pins[], value[]):
	"""Sets an array of pin numbers to a corresponding value according to a seperate an array"""
	for i in range(pins):			#cycles through pin numbers
		newVal=LOW
		if value[i]:
			newVal=HIGH
		setRegisterPin(pins[i], newVal)  #sets pin to the value at a corresponding value of the second array
	writeRegisters()  					#physically changes pin values