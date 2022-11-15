import numpy as np
from itertools import zip_longest




"""Function to perform the Transpose of given input string.  This takes a string
(that reads from left to right) and performs the operation of 'flipping' this string
over its diagonal i.e. input string 'hello' will read DOWNWARDS"""
def transpose(instream, rotate=False):
	#Transposes strings
	stripped = [l.rstrip() for l in instream.split('\n')]
	transposed = map(''.join, zip_longest(*stripped, fillvalue=' '))
	if rotate:
		transposed = reversed(list(transposed))
	return '\n'.join(transposed)




"""Function that mirrors string along the Z-Plane into eyes, i.e the input string
'hello' will now read 'olleh' """
def mirror(instream, vertical=False):
	#Mirrors strings (horizontally by default)
	if vertical:
		#Can preserve trailing whitespace
		unstripped = instream.split('\n')
		mirrored = reversed(unstripped)
	else:
		#Relies on padding => needs a strip
		stripped = [l.rstrip() for l in instream.split('\n')]
		maxlen = max(len(l) for l in stripped)
		padded = [l.ljust(maxlen) for l in stripped]
		mirrored = [l[::-1] for l in padded]
	return '\n'.join(mirrored)




"""Function that takes the mirror of the original input string and performs the
transpose of said string i.e reads UPWARDS"""
def rotate(instream):
	#Rotates strings by 90 degrees, counterclockwise
	return transpose(instream, rotate=True)




#-----------------------------------------------------------------------------------




def mainTest():
    test = "//"
    print("NORMAL")
    print(test)
    print("TRANSPOSE")
    print(transpose(test))
    print("MIRROR")
    print(mirror(test))
    print("ROTATE")
    print(rotate(test))
    return 
#print(mainTest())






