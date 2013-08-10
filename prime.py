#!/usr/bin/env python

import os

def _clear_screen():
    os.system(['clear','cls'][os.name=='nt'])

def prime(x):
    x = abs(int(x))
    if x < 2:
        return True
    if not x & 1:
        return False
    for n in range(3, int(x**0.5)+1, 2):
         if x % n ==0:
             return False
    return True
_clear_screen()
def loop():
	print "Prime numbers. True=prime, False=composite.CTRL=D=exit" 
	x = 1
	while x == 1:
		num = input("Input number: ")
		print prime(num)
loop()
