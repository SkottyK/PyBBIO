"""sevenSeg.py - Scott K 11/6/12
   Object for use with a seven segment display connected to a shift register
   for use with beagle bone
"""

#-----------------------------------------------------------------------------

from bbio import *
from shiftRegister import *

class shiftRegister(object):

    def _init_(self, ser=8, rclk=9, srclk=10, numSeg=1, abcdefg={0,1,2,3,4,5,6,7}):
        disp=new shiftRegister(ser, rclk, srclk, numSeg)
        self.a=abcdefg[0]
