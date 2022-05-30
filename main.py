'''

main.py - main file of isad-assignment

'''

import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from manipulateStrings import *
#from convertNumbers import *
from inputs import *
import re
import os

def main():

    validnumber = 'null'
    haha = "null"

    # Menu
    
    print("\nWelcome to ISAD Assignment.\n\nPlease hold for an operator.")

    # INPUT TYPE
    print("\n(A) Parameter - Input is a set parameter outlined in info.txt\n(B) Keyboard Input - Random user input\n(C) File - Input is from inputFile.txt\n")

    try:
        x = input('')
    except ValueError:
        print('Yeah, nah bro.')
    while x !='A' and x !='B' and x !='C': #A = Parameter, B = Keyboard, C = File
        print('Invalid Selection')
        try:
            x = input('')
        except ValueError:
            print('Yeah, nah bro.')

    input_type = x
    x = ''

    if input_type == 'A':
        input_type_written = 'Parameter'
    elif input_type == 'B':
        input_type_written = 'Keyboard Input'
    elif input_type == 'C':
        input_type_written = 'File'

    print('\nYou have selected input type:', input_type_written)

    # CHOOSE CATEGORY

    try:
        x = input('Choose Category\n(A) Category 1\n(B) Category 2\n\n')
    except ValueError:
        print('Yeah, nah bro.')
    while x !='A' and x !='B': #A = Category 3, B = Category 2
        print('Invalid Selection')
        try:
            x = input('')
        except ValueError:
            print('Yeah, nah bro.')

    func_category = x
    x = ''

    if func_category == 'A':
        func_category_written = 'Category 1'
        print("\nYou have selected Category 1")
    elif func_category == 'B':
        func_category_written = 'Category 2'
        print("\nYou have selected Category 2")

    # CHOOSE FUNCTION
    ############################### CATEGORY 1 #######################################################
    if func_category == 'A':
        try:
            x = input('\n\nCategory A:\n(A) Convert String to Upper Case or Lower Case\n(B) Identify whether numeric values are in a given string\n(C) Identify whether a given string is a valid number or not.\n(D) Remove any numeric values in a given string and then convert the string to upper case or lower Case\n\n')
        except ValueError:
            print('Yeah, nah bro.')
        while x !='A' and x !='B' and x !='C' and x !='D': #A = Convert String to Upper Case or Lower Case, B = Identify whether numeric values are in a given string, C = Identify whether a given string is a valid number or not, D = Remove any numeric values in a given string and then convert the string to upper case or lower Case
            print('Invalid Selection')
            try:
                x = input('')
            except ValueError:
                print('Yeah, nah bro.')

        function_chose = x
        x = ''

        if function_chose == 'A':
            function_chose_written = 'Convert String to Upper Case or Lower Case'
            print('\nYou have chosen function:', function_chose_written)
            try:
                x = input('(A) Make string uppercase, (B) Make string lowercase\n\n')
            except ValueError:
                print('Yeah, nah bro.')
            while x !='A' and x !='B': #A = Upper Case, B = Lower Case
                print('Invalid Selection')
                try:
                    x = input('')
                except ValueError:
                    print('Yeah, nah bro.')
            if x == 'A':
                #Make String Uppercase!
                #PRINT STRING
                print("\nOutput:", convertstring.upper())
            elif x == 'B':
                #Make String Lowercase!
                #PRINT STRING
                print("\nOutput:", convertstring.lower())
        elif function_chose == 'B':
            function_chose_written = 'Identify whether numeric values are in a given string'
            print('\nYou have chosen function:', function_chose_written)
            if input_type == 'B':
                x = input('Enter a string to check if there are numeric values:\n')
                print('\nOutput:', indentifyNumerals(x))
            elif input_type == 'A' or 'C':
                x = indentifyNumerals(identifyifnumerals)
                print('\nOutput:', x)
        elif function_chose == 'C':
            function_chose_written = 'Identify whether a given string is a valid number or not.'
            print('\nYou have chosen function:', function_chose_written)
            try:
                if input_type == 'B':
                    x = input('Enter a string to check if there are numeric values:\n')
                    validnumber = x
                elif input_type == 'A' or 'C':
                    x = validatenumber
                    validnumber = x
                if x != '1' and x != '2' and '3':
                    print('Output: Number or input is invalid\nInput:', validnumber)
                    print('Clarification: Valid numbers were 1,2 or 3')
                else:
                    print('Output: Number is valid\nInput:', validnumber)
                    print('Clarification: Valid numbers were 1,2 or 3')  
            except ValueError:
                pass   
            #INPUT VALID NUMBER

        elif function_chose == 'D':
            function_chose_written = 'Remove any numeric values in a given string and then convert the string to upper case or lower Case'
            print('\nYou have chosen function:', function_chose_written)
            pattern = r'[0-9]'
            try:
                x = input('(A) Make string uppercase and remove numeric values\n(B) Make string lowercase and remove numeric values\n')
            except ValueError:
                print('Yeah, nah bro.')
            while x !='A' and x !='B': #A = Upper Case + Remove Number , B = Lower Case + Remove Number
                print('Invalid Selection')
             
            if input_type == 'B':
                y = input('Input a string.\n')
                validnumber = y
            elif input_type == 'A' or 'C':
                y = numthencaseme
                validnumber = y

            if x == 'A':
                print("\nInput:", validnumber)
                nodigits = re.sub(pattern, '', validnumber)
                print("\nOutput:", nodigits.upper())
            elif x == 'B':
                print("\nInput:", validnumber)
                nodigits = re.sub(pattern, '', validnumber)
                print("\nOutput:", nodigits.lower())
####################################################################################################################################
############################################ CATEGORY 2 ############################################################################
 
    elif func_category == 'B':
        try:
             x = input('\n\nCategory B:\n(A) Convert between meters and feet, or centimeters and inches\n(B) Convert between kilos and pounds, or miligrams and ounces\n(C) Convert between hours and minutes, or minutes and seconds\n\n')
        except ValueError:
            print('Yeah, nah bro.')
        while x !='A' and x !='B' and x !='C': #A = Meters/Feet & Centermeters/Inches, B = Kilos/Pounds & Miligrams/Ounces, C = Hours/Minutes & Minutes/Seconds
            print('Invalid Selection')
            try:
                x = input('')
            except ValueError:
                print('Yeah, nah bro.')

        function_chose = x
        x = ''
################################## FUNCTION (A) ###########################################################
        if function_chose == 'A':
            function_chose_written = 'Meters/Feet, Centimeters/Inches'
            print('\nYou have chosen function:', function_chose_written)
            try:
                x = input('(A) Select Meters/Feet,\n(B) Select Centimeters/Inches\n')
            except ValueError:
                print('Yeah, nah bro.')
            while x !='A' and x !='B':
                print('Invalid Selection')
                try:
                    x = input('')
                except ValueError:
                    print('Yeah, nah bro.')

            if x == 'A': #METERS/FEET
                print("\nYou have chosen meters/feet")
                try:
                    x = input('(A) Select Meters to Feet,\n(B) Select Feet to Meters\n')
                except ValueError:
                    print('Yeah, nah bro.')
                while x !='A' and x !='B':
                    print('Invalid Selection')
                    try:
                        x = input('')
                    except ValueError:
                        print('Yeah, nah bro.')

                if input_type == 'B':
                    y = input('Input a string.\n')
                    validnumber = y
                elif input_type == 'A' or 'C':
                    y = metfeeceninc
                    validnumber = y

                if x == 'A': #METERS TO FEET
                    printable = y, "meters =", float(y) * 3.281, "feet"
                    print('Output:', printable)

                elif x == 'B': #FEET TO METERS
                    printable = y, "feet =", float(y) / 3.281, "meters"
                    print('Output:', printable)

            if x == 'B': #CENTIMETERS/INCHES
                print("\nYou have chosen Centimeters/Inches")
                try:
                    x = input('(A) Select Centimeters to Inches,\n(B) Select Inches to Centimeters\n')
                except ValueError:
                    print('Yeah, nah bro.')
                while x !='A' and x !='B':
                    print('Invalid Selection')
                    try:
                        x = input('')
                    except ValueError:
                        print('Yeah, nah bro.')

                if input_type == 'B':
                    y = input('Input a string.\n')
                    validnumber = y
                elif input_type == 'A' or 'C':
                    y = metfeeceninc
                    validnumber = y

                if x == 'A': #centimeters TO inches
                    printable = y, "centimeters =", float(y) / 2.54, "inches"
                    print('Output:', printable)

                elif x == 'B': #inches TO centimeters
                    printable = y, "inches =", float(y) * 2.54, "centimeters"
                    print('Output:', printable)
###################### FUNCTION B ##########################

        elif function_chose == 'B':
            function_chose_written = 'Kilos/Pounds, Miligrams/Ounces'
            print('\nYou have chosen function:', function_chose_written)
            try:
                x = input('(A) Select Kilos/Pounds,\n(B) Select Miligrams/Ounces\n')
            except ValueError:
                print('Yeah, nah bro.')
            while x !='A' and x !='B':
                print('Invalid Selection')
                try:
                    x = input('')
                except ValueError:
                    print('Yeah, nah bro.')

            if x == 'A': #METERS/FEET
                print("\nYou have chosen Kilos/Pounds")
                try:
                    x = input('(A) Select Kilos to Pounds,\n(B) Select Pounds to Kilos\n')
                except ValueError:
                    print('Yeah, nah bro.')
                while x !='A' and x !='B':
                    print('Invalid Selection')
                    try:
                        x = input('')
                    except ValueError:
                        print('Yeah, nah bro.')

                if input_type == 'B':
                    y = input('Input a string.\n')
                    validnumber = y
                elif input_type == 'A' or 'C':
                    y = kilopoundmiliounc
                    validnumber = y

                if x == 'A': #Kilos TO Pounds
                    printable = y, "Kilos =", float(y) * 2.205, "Pounds"
                    print('Output:', printable)

                elif x == 'B': #FEET TO METERS
                    printable = y, "Pounds =", float(y) / 2.205, "Kilos"
                    print('Output:', printable)

            if x == 'B': #Miligrams/Ounces
                print("\nYou have chosen Miligrams/Ounces")
                try:
                    x = input('(A) Select Miligrams to Ounces,\n(B) Select Ounces to Miligrams\n')
                except ValueError:
                    print('Yeah, nah bro.')
                while x !='A' and x !='B':
                    print('Invalid Selection')
                    try:
                        x = input('')
                    except ValueError:
                        print('Yeah, nah bro.')

                if input_type == 'B':
                    y = input('Input a string.\n')
                    validnumber = y
                elif input_type == 'A' or 'C':
                    y = kilopoundmiliounc
                    validnumber = y

                if x == 'A': #Miligrams TO Ounces
                    printable = y, "Miligrams =", float(y) / 28350, "Ounces"
                    print('Output:', printable)

                elif x == 'B': #inches TO centimeters
                    printable = y, "inches =", float(y) * 28350, "centimeters"
                    print('Output:', printable)
###################### FUNCTION C ######################################

        elif function_chose == 'C':
            function_chose_written = 'Hours/Minutes, Minutes/Seconds'
            print('\nYou have chosen function:', function_chose_written)
            try:
                x = input('(A) Select Hours/Minutes,\n(B) Select Minutes/Seconds\n')
            except ValueError:
                print('Yeah, nah bro.')
            while x !='A' and x !='B':
                print('Invalid Selection')
                try:
                    x = input('')
                except ValueError:
                    print('Yeah, nah bro.')

            if x == 'A': #METERS/FEET
                print("\nYou have chosen Hours/Minutes")
                try:
                    x = input('(A) Select Hours to Minutes\n(B) Select Minutes to Hours\n')
                except ValueError:
                    print('Yeah, nah bro.')
                while x !='A' and x !='B':
                    print('Invalid Selection')
                    try:
                        x = input('')
                    except ValueError:
                        print('Yeah, nah bro.')

                if input_type == 'B':
                    y = input('Input a string.\n')
                    validnumber = y
                elif input_type == 'A' or 'C':
                    y = kilopoundmiliounc
                    validnumber = y

                if x == 'A': #Hours TO Minutes
                    printable = y, "Hours =", float(y) * 60, "Minutes"
                    print('Output:', printable)

                elif x == 'B': #Minutes TO Hours
                    printable = y, "Minutes =", float(y) / 60, "Hours"
                    print('Output:', printable)

            if x == 'B': #Minutes/Seconds
                print("\nYou have chosen Minutes/Seconds")
                try:
                    x = input('(A) Select Minutes to Seconds,\n(B) Select Seconds to Minutes\n')
                except ValueError:
                    print('Yeah, nah bro.')
                while x !='A' and x !='B':
                    print('Invalid Selection')
                    try:
                        x = input('')
                    except ValueError:
                        print('Yeah, nah bro.')

                if input_type == 'B':
                    y = input('Input a string.\n')
                    validnumber = y
                elif input_type == 'A' or 'C':
                    y = kilopoundmiliounc
                    validnumber = y

                if x == 'A': #Minutes TO Seconds
                    printable = y, "Minutes =", float(y) * 60, "Seconds"
                    print('Output:', printable)

                elif x == 'B': #Seconds TO Minutes
                    printable = y, "Seconds =", float(y) / 60, "Minutes"
                    print('Output:', printable)



if __name__ == "__main__":
    main()


# OPTIONS PLAN

'''
OPTIONS A:
(A) Parameter
(B) Keyboard 
(C) File

|
v

OPTIONS B:
(A) Category A
(B) Category B

|
v

OPTIONS C,A:
(A)
(B)
(C)
(D)

OR

OPTIONS C,B:
(A)
(B)
(C)

|
v


INPUT (B EXCLUSIVE)

|
v

OUTPUT

|
v

VISUAL OUTPUT (AA,AB)

|
v

FILE OUTPUT (AC)


'''

