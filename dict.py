#from curses.ascii import isspace
import numpy as np
from grid import ABC, DEF, GHI
from grid import JKL, MNO, PQR
from grid import STUV, WXYZ



abcL = ABC()
defL = DEF()
ghiL = GHI()
jklL = JKL()
mnoL = MNO()
pqrL = PQR()
stuvL = STUV()
wxyzL = WXYZ()


#Dictionary set up in the format {value : key}


newAlphabet = {

    #Standard alphabet input
    "a" : abcL[0],
    "b" : abcL[1],
    "c" : abcL[2],

    "d" : defL[0],
    "e" : defL[1],
    "f" : defL[2],

    "g" : ghiL[0],
    "h" : ghiL[1],
    "i" : ghiL[2],

    "j" : jklL[0],
    "k" : jklL[1],
    "l" : jklL[2],

    "m" : mnoL[0],
    "n" : mnoL[1],
    "o" : mnoL[2],

    "p" : pqrL[0],
    "q" : pqrL[1],
    "r" : pqrL[2],

    "s" : stuvL[0],
    "t" : stuvL[1],
    "u" : stuvL[2],
    "v" : stuvL[3],

    "w" : wxyzL[0],
    "x" : wxyzL[1],
    "y" : wxyzL[2],
    "z" : wxyzL[3],


    #Extra required symbols
    "\u0020" :  int(2.5)*"\u0020", #2x amount of space between words (increase readability)
    "." : ".", #full stop for sentences
    "\n" : "\n", #for purpose of translating .txt documents (space end of sentence)
    "," : "," #comma

}


"""Inverted dictionary below utilized when transforming back from new language
to standard alphabet implementation"""
newAlphabetInvert = { y:x for (x,y) in newAlphabet.items() }
#print(newAlphabetInvert)



