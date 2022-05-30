'''

manipulateStrings.py - contains category 1 functions for main.py program


Requirements:
a. Converting a given string to upper case or lower case.

b. Identify whether numeric values are in a given string.

c. Identify whether a given string is a valid number or not.

d. Remove any numeric values in a given string and then convert the string to upper case or lower Case. 

'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

# (A) Converting a given string to upper case or lower case.

#def changeCase(mf):

# Already done by .lower() and .upper()


# (B) Identify whether numeric values are in a given string.

def indentifyNumerals(inputString):
    return any(char.isdigit() for char in inputString)


# (C) Identify whether a given string is a valid number or not.

#def validNumber(row):


# (D) Remove any numeric values in a given string and then convert the string to upper case or lower Case. 

#def deez(row):


#