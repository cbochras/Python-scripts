# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:34:13 2021

"""

############### Finger exercise:                     ##################
"""Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside 
a for loop that iterates over the odd integers between 3 and 999."""

for j in range(3,50):
    if(j%2==0):
        print(j,'is an even number')
        
        
        
        
####################
## EXAMPLE: guess and check cube root  ??????????????????????
###################
# cube = 27
# ##cube = 8120601
# #for guess in range(abs(cube)+1):
# #    # passed all potential cube roots
# guess=int(input(' guess a number for the cube root of 27 '))
# if guess**3 >= abs(cube):
#     break 
#         # no need to keep searching
# print('Cube root of ' + str(cube) + ' is ' + str(guess))
       
# if guess**3 != abs(cube):
#     print(cube, 'is not a perfect cube')
# else:
#     if cube < 0:
#         guess = -guess
        
####################
## EXAMPLE: guess and check cube root   WHILE  ###################
####################
x=int(input(' enter an int number(0-999) : '))
ans=0
if x>0 and x<1000:
    while ans**3<=abs(x):
        ans=ans+1
#        print(ans)
        
        if ans**3== abs(x):
            print('Cube root of ' + str(x) + ' is ' + str(ans))
            break
        
        elif(ans**3>abs(x)):
            print(x, 'is not a perfect cube')        
else :
    print('please, enter a number as specified' )       
    
################################## FOR  #######
x=int(input(' enter an int number(0-999) : '))

for guess in range(int(abs(x)/2)): #cube root must be less than half of that number
    if guess**3== abs(x):
        if(x<0):
            guess=-guess
        print('Cube root of ' + str(x) + ' is ' + str(guess))
        break
    elif(guess**3>abs(x)):
            print(x, 'is not a perfect cube') 
            break
###########################################################
#####  PRIME NUMBERS
""" The simplest way to find out if an integer, x, greater than 3 is
prime, is to divide x by each integer between 2 and, x-1. If the
remainder of any of those divisions is 0, x is not prime, otherwise x is
prime. """

x=int(input(' enter an int number(0-999) : '))
smallest_divisor=None
for guess in range(2,abs(x)):
    if(x%guess==0):
        print(guess) # optional
        smallest_divisor=guess
        break
if (smallest_divisor!=None):
    print(x,' is not a prime number')  
else:
    print(x,' is a prime number')                   
   
##########################   FLOAT NUMBERS   ##################

x = 0.0
for i in range(11):
    x = x + 0.1
    if x == 1.0:
        print(x, '= 1.0')
    else:
        print(x, 'is not 1.0')

################    Functions and Scoping    ########################

import time
def max_val(x, y):
    if x > y:
        return x
    else:
        return y
x,y=5,8
print(max_val(x, y))
#time.sleep(2)

a,b=32,25
print(max_val(a, b))
#time.sleep(2)

print(max_val(b, a))

##########################################################
##########     Keyword Arguments and Default Values    ###########
"""In Python, there are two ways that formal parameters get bound to
actual parameters. The most common method, which is the one we
have used so far, is called positional—the first formal parameter is
bound to the first actual parameter, the second formal to the second
actual, etc. Python also supports keyword arguments, in which
formals are bound to actuals using the name of the formal
parameter. Consider the function definition"""

def print_name(first_name, last_name, reverse):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)


print_name('Olga', 'Puchmajerova', True)
print_name('Olga', 'Puchmajerova', reverse = False)
print_name('Olga', last_name = 'Puchmajerova', reverse = False)
print_name(last_name = 'Puchmajerova', first_name = 'Olga', reverse = False)
print_name('Olga', 'Puchmajerova')
# Puchmajerova, Olga
# Olga Puchmajerova
# Olga Puchmajerova
# Olga Puchmajerova


"""Default values allow programmers to call a function with fewer
than the specified number of arguments. For example,"""

print_name('Olga', 'Puchmajerova', True)
print_name('Olga', 'Puchmajerova', reverse = True)
print_name('Olga', 'Puchmajerova')   # reverse argument missing error !!!

"""Keyword arguments are commonly used in conjunction with
default parameter values. We can, for example, write"""

def print_name(first_name, last_name, reverse = False): # if no any argument for reverse, default is none)
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)

print_name('Olga', 'Puchmajerova')
print_name('Olga', 'Puchmajerova', False)
print_name('Olga', 'Puchmajerova', reverse = False)
print_name('Olga', 'Puchmajerova', reverse = True)

#############Finger exercise: ######################
"""Write a function mult that accepts either one or
two ints as arguments. If called with two arguments, the function
prints the product of the two arguments. If called with one argument,
it prints that argument."""

def mult(arg_1,arg_2 = False ):
    if arg_2:
        print(arg_1*arg_2)
    else:
        print(arg_1)
        
mult(5,3)
mult(4,2)
mult(7)

# 15
# 8
# 7

#####################    Variable Number of Arguments  #################
"""Python has a number of built-in functions that operate on a variable
number of arguments. For example,"""
min(6,4)
min(3,4,1,6)


"""The unpacking operator
* allows a function to accept a variable number of positional
arguments. For example,"""


def mean(*args):
# Assumes at least one argument and all arguments are numbers
# Returns the mean of the arguments
    total = 0
    for a in args:
        total += a
    return total/len(args) # care about indent here !!!!
    
mean(5,6,7,8)  # 6.5

print(mean(5,6,7,8,1,9,12))
#####################     Scoping    ##########################
#Let's look at another small example:


def f(x): #name x used as formal parameter
    y = 1
    x = x + y
    print('x =', x)
    return x
x = 3
y = 2
z = f(x) #value of x used as actual parameter
print('z =', z)
print('x =', x)
print('y =', y)

# x = 4
# z = 4
# x = 3
# y = 2

"""Each function defines a new name space, also called a scope. The formal
parameter x and the local variable y that are used in f exist only
within the scope of the definition of f. The assignment statement x =
x + y within the function body binds the local name x to the object 4.
The assignments in f have no effect on the bindings of the names x
and y that exist outside the scope of f.
Here's one way to think about this:"""
"""
1. At the top level, i.e., the level of the shell, a symbol table
keeps track of all names defined at that level and their current
bindings.
2. When a function is called, a new symbol table (often called a
stack frame) is created. This table keeps track of all names
defined within the function (including the formal parameters)
and their current bindings. If a function is called from within
the function body, yet another stack frame is created.
3. When the function completes, its stack frame goes away. """

def f(x):
    def g():
        x='abc'
        print('x=',x)
    def h():
        z=x
        print('z=',z)
    x=x+1
    print('x=',x)
    h()
    g()
    print('x=',x)
    return g

x=3
z=f(x)
print('x=',x)
print('z=',z)
z()
# output
# x= 4
# z= 4
# x= abc
# x= 4
# x= 3
# z= <function f.<locals>.g at 0x00000223FB535D30>
# x= abc

#############################
def f(x):
    def g():
        x='abc'
        print('x=',x)
       
    
    x=x+1
    print('x=',x)
   
    g()
    print('x=',x)
    

x=3
z=f(x)

# outputs
# x=4
# x=abc
# x=4

#############################
def f(x):
    def g():
        x='abc'
        print('x=',x)
       
    
    x=x+1
    print('x=',x)
   
    g()
    print('x=',x)
    

x=3
z=f(x)
print('x=',x)


# output
# x=4
# x=abc
# x=4
# x=3

#############################
def f(x):
    def g():
        x='abc'
        print('x=',x)
       
    
    x=x+1
    print('x=',x)
   
    g()
    print('x=',x)
    

x=3
z=f(x)
print('x=',x)
print('z=',z)

# output
# x=4
# x=abc
# x=4
# x=3
# z=None # z=f(x) calls g() does not produce a
# return value

#############################
def f(x):
    def g():
        x='abc'
        print('x=',x)
       
    
    x=x+1
    print('x=',x)
   
    g()
    print('x=',x)
    return g

x=3
z=f(x)
print('x=',x)
print('z=',z)

# output
# x=4
# x=abc
# x=4
# x=3
#z= <function f.<locals>.g at 0x00000223FB535D30>


#############################
def f(x):
    def g():
        x='abc'
        print('x=',x)
        
    
    x=x+1
    print('x=',x)
   
    g()
    print('x=',x)
    return x

x=3
z=f(x)
print('x=',x)
print('z=',z)

# output
# x=4
# x=abc
# x=4
# x=3
# z=4

#############################

def f(x):
    def g():
        x='abc'
        print('x=',x)
        
    
    x=x+1
    print('x=',x)
   
    g()
    print('x=',x)
    return g

x=3
z=f(x)
print('x=',x)
print('z=',z)

# output
# x=4
# x=abc
# x=4
# x=3
# z= <function f.<locals>.g at 0x00000223FB535430>

#############################

def f(x):
    def g():
        x='abc'
        print('x=',x)
        
    
    x=x+1
    print('x=',x)
   
    g()
    print('x=',x)
    return g

x=3
z=f(x)
print('x=',x)
print('z=',z)
z()
# output
# x=4
# x=abc
# x=4
# x=3
# z= <function f.<locals>.g at 0x00000223FB535430>
# x=abc   z() produces this

#############################
def f(x):             #line 1
    def g():          #line 2
        x='abc'       #line 3
        print('x=',x) #line 4
    def h():          #line 5
        z=x           #line 6
        print('z=',z) #line 7
    x=x+1             #line 8
    print('x=',x)     #line 9
    h()               #line 10
    g()               #line 11
    print('x=',x)     #line 12
    return g          #line 13

x=3                   #line 14
z=f(x)                #line 15
print('x=',x)         #line 16
print('z=',z)         #line 17  returns with g
z()                   #line 18

# x= 4  line 15 result:  execution order  1,8,9
# z= 4                then 10,5,6,7
# x= abc              then 11,2,3,4
# x= 4                then 12
# x= 3  line 16 result:  execution order 
# z= <function f.<locals>.g at 0x00000223FB535670>
# x= abc  line 18 result:  execution order 2,3,4
#note: z=g() from line 17


#############################
def f(x):
    def g():
        x='abc'
        print('x=',x)
    
    x=x+1
    print('x=',x)
    return x**2

x=3
z=f(x)         # outputs  x=4
print('x=',x)  # outputs  x=3
print('z=',z)  # outputs  z=16

################  CAN WE ACCESS g() DIRECTLY ???  NO
def f(x):
    def g():
        x='abc'
        print('x=',x)
    
    x=x+1
    print('x=',x)
    return x**2

x=3
z=f(x)         # outputs  x=4
print('x=',x)  # outputs  x=3
print('z=',z)  # outputs  z=16
g()  NameError: name 'g' is not defined

############### WE CAN ACCESS g() INDIRECTLY
def f(x):
    def g():
        x='abc'
        print('x=',x)
    
    x=x+1
    print('x=',x)
    return g

x=3
z=f(x)         # outputs  x=4
print('x=',x)  # outputs  x=3
z() # z=f(x) returns g, so, g() is binded to z()
# and produces x=abc
# outputs:
# x= 4
# x= 3
# x= abc

