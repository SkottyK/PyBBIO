"""sevenSegShift.py - Scott K 11/6/12
   Object for use with a seven segment display connected to a shift register
   for use with beagle bone

   *note this is meant to control 1 digit per register, not multiple digit displays
"""

#-----------------------------------------------------------------------------

from bbio import *
from shiftRegister import *

class sevenSegShift(object):

    


    def _init_(self, ser=8, rclk=9, srclk=10, anodeCathode=1, numDisp=1, abcdefgp={0,1,2,3,4,5,6,7,8}):
        """Initialized necessary variables for sevenSegShift class"""
      
        #creates new shift register object per display
        
        dispList = [ ShiftRegister(ser, rclk, srclk) for i in range(numDisp)]

        self.a=abcdefg[0]
        self.b=abcdefg[1]
        self.c=abcdefg[2]
        self.d=abcdefg[3]
        self.e=abcdefg[4]
        self.f=abcdefg[5]
        self.g=abcdefg[6]
        self.dp=abcdefg[7]

        if anodeCathode==0:
            self.ON=HIGH
            self.OFF=LOW
        else:
            self.ON=LOW
            self.OFF=HIGH

    def setDigit(self, char, disp):
        if disp<
