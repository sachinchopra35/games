# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:20:53 2021

@author: Sachin
"""

#Sachin's Grand National

#%%

#import numpy as np
import random

#%%

#initialise positions

Arun = 0
Rohan = 0
Sachin = 0
Beesh = 0

#%%

def pickACard(Arun, Rohan, Sachin, Beesh):
    x = random.randint(1,5)
    if x == 1:
        Arun += 1
        print("@aruntheninja moved forward")
    elif x == 2:
        Rohan += 1
        print("Extortion moved forward")
    elif x == 3:
        Sachin += 1
        print("The MACHINE aka Dunch moved forward")
    elif x == 4:
        Beesh += 1
        print("Beeshy boi moved forward")
    elif x==5:
        y = random.randint(1,4)
        if y == 1 and Arun >= 1:
            Arun -= 1
            print("@aruntheninja moved ***backwards***")
        elif y == 2 and Rohan >= 1:
            Rohan -= 1
            print("Extortion moved ***backwards***")
        elif y == 3 and Sachin >= 1:
            Sachin -= 1
            print("The MACHINE aka DUNCH moved ***backwards***")
        elif y == 4 and Beesh >= 1:
            Beesh -= 1
            print("Beeshy boi moved ***backwards***")
        else:
            print("Nobody moved (since you can't go to position -1)")
        
    print("Current positions:", "\n Arun:", Arun, "\n Rohan:", Rohan,"\n Sachin:", Sachin,"\n Beesh:", Beesh)
    return Arun, Rohan, Sachin, Beesh
    
#%%

finish_line = 10

print()

Arun, Rohan, Sachin, Beesh = pickACard(Arun, Rohan, Sachin, Beesh)



if Arun >= finish_line:
    print("***ARUNTHENINJA WON*** \n WOOOOOOOOOO")
if Rohan >= finish_line:
    print("***EXTORTION WON*** \n WOOOOOOOOOOO")
if Sachin >= finish_line:
    print("***DUNCH WON*** \n WOOOOOOOOOO")
if Beesh >= finish_line:
    print("***BEESH WON*** \n WOOOOOOOOOOOOO")

print()

#%%