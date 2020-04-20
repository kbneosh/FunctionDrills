'''
Created on Apr 20, 2020

@author: ITAUser
'''
'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with FUNCTIONS.
Focus on the functions and find the problems with the FUNCTIONS.

For this debug, there could be problems with executing the functions. For example,
calling the function may have been done wrong, or put in the wrong spot. So don't
just look at the function itself but also the line calling the function.

Additionally, if converting becomes difficult, ask the instructor about how to
use a conversion table or other tricks to help make sure the conversion is right.

The number of errors are as follows:
ouncesToGallons: 4
gallonsToOunces: 6
gramsToPounds: 4
poundsToGrams: 4
'''

#The problems are between the two --- lines
#-------------------------------------------------

'''
This function converts ounces to gallons using three steps.
'''
def ounces_to_gallons(num1):
    #There are eight ounces in a cup
    divideNum = num1 / 128
    return divideNum
x = ounces_to_gallons(24)
print (x)

#------------------------------------------------


#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts gallons to ounces using three steps.
'''
def gallons_to_ounces(num1):
    #There are four quarts in a gallon
    productOfNums = num1 * 128
    return productOfNums
x = gallons_to_ounces(24)
print(x)


#------------------------------------------------



#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts grams to pounds using two steps.
'''
def grams_to_pounds(num1):
    #There are 16 grams in one pound
    productOfnums = num1 / 454
    return productOfnums
x = grams_to_pounds(360)
print(x)

#------------------------------------------------


#The problems are between the two --- lines
#-------------------------------------------------
#This function converts pounds to grams using two steps.
'''

ghvgfyt
'''
def pounds_to_grams(num1):
    #There are 16 ounces in one pound
    productOfnums = num1 * 454
    return productOfnums
x = pounds_to_grams(360)
print(x)
#------------------------------------------------
