# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:20:44 2021

@author: umit
"""

##############      RECURSION AND GLOBAL VARIABLES     #######
# Recursion method: using the repetitive function call inside of that function/

def fact_iter(n):   #NORMAL ITERATION
    """Assumes n an int > 0
    Returns n! """
    result = 1
    for i in range(1,n+1):
        result*= i
    return result
    
print(fact_iter(5))     # 720

#OR
def fact_iter(n):   #NORMAL ITERATION


    """Assumes n an int > 0
    Returns n! """
    result = 1
    for i in range(1,n+1):
        result*= i
    print(result)
    
fact_iter(5)









# Recursion method: using the repetitive function call 
# inside of that function


# """Assumes n an int > 0    Returns n! """   
def fact_rec(n):
   
    # if n==1:     # this line must be exist, otherwise, loop goes to infinitive
    #     return n
    # else:
        return n*fact_rec(n-1)
    
print(fact_rec(5))     # 720    

# how it works ?
"""In first loop, n=5  then in the line "return n*fact_rec(n-1)",
5*fact_rec(4)  means we call the function:fact_rec(n=4), next time
4*fact_rec(3)  means we call the function:fact_rec(n=3), next time
3*fact_rec(2)  means we call the function:fact_rec(n=2), next time
2*fact_rec(1)  means we call the function:fact_rec(n=1), returns 1,
then backward 2*3*4*5 = 120""

####   Finger exercise: 
"""The harmonic sum of an integer, n > 0, can be
calculated using the formula 1+1/2 +...+1/n . Write a recursive function
that computes this."""


def sum_iter(n):   #NORMAL ITERATION
    """Assumes n an int > 0
    Returns 1+1/2 + ...+ 1/n """
    result = 0
    for i in range(1,n+1):
        result+= 1/i
    return result
    
print(sum_iter(5))   # 2.2833333333333


def sum_iter(n):   #NORMAL ITERATION
    """Assumes n an int > 0
    Returns 1+1/2 + ...+ 1/n """
    result = 0
    for i in range(1,n+1):
        result+= 1/i
    return result
    
print(sum_iter(8))  # 2.7178571428571425





def sum_rec(n):  ####  RECURSIVE 
   
    if n==1:
        return n
    else:
        return (1/n +sum_rec(n-1))
    
print(sum_rec(5))  # 2.283333333333
    

################    MODULES AND FILES  #######

""" Modules are typically stored in individual files. Each module has
its own private symbol table. Consequently, within circle_formulas.py we
access objects (e.g., pi and area) in the usual way. Executing import
M creates a binding for module M in the scope in which the import
appears. Therefore, in the importing context we use dot notation to
indicate that we are referring to a name defined in the imported
module. For example, outside of circle_formulas.py, the references pi and
circle_formulas.pi can (and in this case do) refer to different objects."""


import circle_formulas 
pi = 3
print(pi)
print(circle_formulas.pi)
print(circle_formulas.area(4))
print(circle_formulas.circumference(4))
print(circle_formulas.sphere_surface(4))
print(circle_formulas.sphere_volume(4))






"""a module can contain executable statements as
well as function definitions. Typically, these statements are used to
initialize the module. For this reason, the statements in a module are
executed only the first time a module is imported into a program.
Moreover, a module is imported only once per interpreter session. If
you start a console, import a module, and then change the contents
of that module, the interpreter will still be using the original version
of the module.

A variant of the import statement that allows the importing
program to omit the module name when accessing names defined
inside the imported module. Executing the statement from M import
* creates bindings in the current scope to all objects defined within M,
but not to M itself. For example, the code"""


from circle_formulas import *   # variables in circle_formulas are imported
print(pi)               # 3,1459
print(circle_formulas.pi)   # NameError: name 'circle_formulas' is not defined
# because, circle_formulas module was not imported, we can refer the variable


"""A commonly used variant of the import statement is
import module_name as new_name
This instructs the interpreter to import the module named
module_name, but rename it to new_name. This is useful if
module_name is already being used for something else in the
importing program."The most common reason programmers use this
form is to provide an abbreviation for a long name.""

########   PYTHON   PREDEFINED PACKAGES  #############
 
"""The Anaconda distribution for Python 3.8 comes with over 600
 packages! NOW,  math and calendar"""

# For example, to print the log of x base 2, all you need to write is

import math
x= 1024
print(math.log(x, 2))   #  10


import calendar as cal
cal_english = cal.TextCalendar()
cal_english2 = cal.Calendar()

print(cal.weekday(2021,2,21))  # 6 (6-Saturday, 0-Sunday)

     
print(cal_english.formatmonth(1949, 3))
outputs:
     March 1949
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31



print(cal.isleap(1953))   # False

print(cal.leapdays(1992,2020))   # 7


print(cal_english2.monthdayscalendar(1999,3))
# output:
#     [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], 
#      [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28],
#      [29, 30, 31, 0, 0, 0, 0]]

print(cal_english.monthdayscalendar(1999,3))
# output:
# [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], 
#  [29, 30, 31, 0, 0, 0, 0]]

