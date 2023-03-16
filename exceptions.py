# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:52:54 2021

@author: umit.tas
"""

###############   EXCEPTIONS AND ASSERTIONS     ####################

An “exception” is usually defined as “something that does not
conform to the norm,” and is therefore somewhat rare. There is
nothing rare about exceptions in Python. They are everywhere.
Virtually every module in the standard Python library uses them, and
Python itself will raise them in many circumstances.

Among the most common types of exceptions are TypeError,
IndexError, NameError, and ValueError.

test = [1,2,3]
test[3]         # IndexError: list index out of range


Exceptions, when raised, can and should be handled by the
program. Sometimes an exception is raised because there is a bug in
the program (like accessing a variable that doesn't exist), but many
times, an exception is something the programmer can and should
anticipate. A program might try to open a file that does not exist. If
an interactive program asks a user for input, the user might enter
something inappropriate.

Python provides a convenient mechanism, try-except, for
catching and handling exceptions. The general form is:
    
 try
 code block
except (list of exception names):
    code block
else:
    code block   
    
If you know that a line of code might raise an exception when
executed, you should handle the exception. In a well-written
program, unhandled exceptions should be the exception.
Consider the code

success_failure_ratio = num_successes/num_failures
print('The success/failure ratio is', success_failure_ratio)
#NameError: name 'num_successes' is not defined

Most of the time, this code will work just fine, but it will fail if
num_failures happens to be zero. The attempt to divide by zero will
cause the Python runtime system to raise a ZeroDivisionError
exception, and the print statement will never be reached.



It is better to write something along the lines of:

num_failures = 0
num_successes = 10

    
try:
    success_failure_ratio = num_successes/num_failures
    print('The success/failure ratio is',success_failure_ratio)
except ZeroDivisionError:
   #print('No failures, so the success/failure ratio is undefined.')    
    print('you are trying to divide with zero')
#prints: No failures, so the success/failure ratio is undefined.
#or prints:you are trying to divide with zero

    
 try block contains a zero division, when we receive it  as an except, the
codes  under this except will be executed . 

# IF MORE EXCEPTION  TYPES  

If it is possible for a block of program code to raise more than one
kind of exception, the reserved word except can be followed by a
tuple of exceptions, e.g.,
except (ValueError, TypeError):
in which case the except block will be entered if any of the listed
exceptions is raised within the try block.

# WRITING MULTIPLE EXCEPT  
Alternatively, we can write a separate except block for each kind
of exception, which allows the program to choose an action based
upon which exception was raised.

    try:
        .......
    except ZeroDivisionError:
        .......
    except:      # if any other exception than ZeroDivisionError , it comes to here !!!!
        .........


######    EXAMPLE

val = int(input('Enter an integer: '))
print('The square of the number you entered is', val**2)

"""If the user obligingly types a string that can be converted to an
integer, everything will be fine. But suppose the user types abc?
Executing the line of code will cause the Python runtime system to
raise a ValueError exception, and the print statement will never be
reached.
What the programmer should have written would look something
like"""


 while True:
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square of the number you entered is',val**2)
        break #to exit the while loop
    except ValueError:
        print(val, 'is not an integer')




    
  ##############    FINGER EXERCISE  ##############


If we type  1+'a'    in shell, we get the error:
  TypeError: unsupported operand type(s) for +: 'int' and 'str'  


try:
    int('a')
    print(1+'a')
    print(5/0)
except TypeError:
    print('integer and string can not be added')
    
except ZeroDivisionError:
    print('an integer can not be divided with Zero')
    
except ValueError:
    print('this is ValueError')
    
    





#####   In case of summing only decimal characters in a string

L=['0','1','2','3','4','5','6','7','8','9']

def sum_digits(s):
    """Assumes s is a string Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""  
    try: 
        total = 0
        for aa in s:
            for ab in L:
                if aa==ab:
                   total+= int(ab)
        return total
    except  TypeError:
        print('You are trying to add different types' )
    

print('total= ',sum_digits('a2b3c'))


###############    Assertions   ##################

The Python assert statement provides programmers with a simple
way to confirm that the state of a computation is as expected. An
assert statement can take one of two forms:
    
assert Boolean expression

or

assert Boolean expression, argument

When an assert statement is encountered, the Boolean
expression is evaluated. If it evaluates to True, execution proceeds on
its merry way. If it evaluates to False, an AssertionError exception is
raised.

Assertions are a useful defensive programming tool. They can be
used to confirm that the arguments to a function are of appropriate
types. They are also a useful debugging tool. They can be used, for
example, to confirm that intermediate values have the expected
values or that a function returns an acceptable value.


Example for   #  AssertionError: x  should be 'hello'

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"      # since x='hello', nothing happens

#if condition returns False, AssertionError is raised:
assert x == "goodbye" ,  "x should be 'hello'" # if x is not 'hello',
# next string will be printed:
    # AssertionError: x should be 'hello'

assert x == "hello" ,  "x should be 'hello'" # since x='hello', 
                                                #nothing happens
                                                
                                                
################################


def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))  # prints:  32.0
print( int(KelvinToFahrenheit(505.78)))     # prints:  451
print(KelvinToFahrenheit(-5))  # 
 # prints: AssertionError: Colder than absolute zero!
 
""" if the condition (Temperature >= 0) is False, then AssertionError
is raised and next message "Colder than absolute zero!" is displayed"""


#######   EXAMPLE  ######   ***********************
Better yet, this function can be generalized to ask for any type of
input:
    
def read_val(val_type, request_msg, error_msg):
    while True:
        val = input(request_msg + ' ')
        try:
            return(val_type(val)) #convert str to val_type
        except ValueError:
            print(val, error_msg)
            
val = read_val(int, 'Enter an integer:', 'is not an integer')  


          
The function read_val is polymorphic, i.e., it works for
arguments of many different types. Such functions are easy to write
in Python, since types are first-class objects. We can now ask for
an integer using the code




 # If input is not an integer, error message: val  is not an integer


With exceptions, the programmer still needs to include code
dealing with the exception. However, if the programmer forgets to
include such code and the exception is raised, the program will halt
immediately. This is a good thing. It alerts the user of the program
that something troublesome has happened. ( overt bugs are much better 
than covert bugs.) Moreover,
it gives someone debugging the program a clear indication of where
things went awry.


###############   Exceptions as a Control Flow Mechanism

Don't think of exceptions as purely for errors. They are a convenient
flow-of-control mechanism that can be used to simplify programs.
In many programming languages, the standard approach to
dealing with errors is to have functions return a value (often
something analogous to Python's None) indicating that something is
amiss. Each function invocation has to check whether that value has
been returned. In Python, it is more usual to have a function raise 
an exception when it cannot produce a result that is consistent with
the function's specification.

The Python raise statement forces a specified exception to
occur. The form of a raise statement is:
    
    raise exceptionName(arguments)
    
 The exceptionName is usually one of the built-in exceptions, e.g.,
ValueError. However, programmers can define new exceptions by
creating a subclass (see Chapter 10) of the built-in class Exception.
Different types of exceptions can have different types of arguments,
but most of the time the argument is a single string, which is used to
describe the reason the exception is being raised.

###   EXAMPLE   ####

def get_grades(fname):
    grades=[]
    try:
        with open(fname,'r') as grades_file:
            for line in grades_file:
                try:
                    grades.append(float(line))
                except:
                    raise ValueError('Cannotconvert line to float')
                
    except IOError:
        raise ValueError('get_grades could not opened' + fname)
    return grades
try:
    grades=get_grades('quiz1grades.txt')
    print(grades) #[24.0, 56.0, 90.0, 45.0, 78.0, 67.0, 16.0]
    grades.sort() # [16.0, 24.0, 45.0, 56.0, 67.0, 78.0, 90.0]
    median = grades[len(grades)//3] # finding the mid value of the list
    print('Median grade is', median) # Median grade is 56.0
except ValueError as error_msg:
    print('Whoop.', error_msg)                           



try:
    grades=get_grades('quiz1grades2.txt') # this file contains 'abc'
                                            # in a line
    print(grades)
    grades.sort()
    median = grades[len(grades)//2]                               
    print('Median grade is', median)
except ValueError as error_msg:
    print('Whoop.', error_msg) # Whoop. Cannotconvert line to float


        
             




#######  Finger exercise: Implement a function that 
#######   satisfies the specification

def find_an_even(L):
    """Assumes L is a list of integers Returns the first even number
    in L  Raises ValueError if L does not contain an even
number"""   









