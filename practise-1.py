# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:21:03 2021

"""
################   IF
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
    

if y != 0:
    print("therefore, x / y is", x/y)

print("thanks!")


n = input("You're in the Lost Forest. Go left or right? ")

while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
    
print("You got out of the Lost Forest!")

n = 0
while n < 5:
    print(n)
    n+=1
    
print('you already reached the max value')








#########################################################
#conditional statements and BRANCHING

x=8

if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')

x=7

if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')

###########################################################

#the nested conditional statements 

x=15  # LAST CONDITION DOESN"T WORK IF X%2=0 ONLY !

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
        
elif x%3 == 0:
    
    print('Divisible by 3 and not by 2') 
  
else:
    print('Divisible by 2 and not by 3')  # ERROR! DOESN"T FUNCTIONING!
    
############################################################

#the nested conditional statements 

x=12

if (x%2 == 0) and (x%3 == 0):
    print('Divisible by 2 and 3')
        
elif x%3 == 0:
    
    print('Divisible by 3 and not by 2') 
  
else:
    print('Divisible by 2 and not by 3')

###########################################################
"""Finger exercise: Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three.
"""
x, y, z = 5,  8,  9

if x%2 != 0 and y%2 != 0 and z%2 != 0:
     print(max(x, y, z))
if x%2 != 0 and y%2 != 0 and z%2 == 0:
    print(max(x, y))
if x%2 != 0 and y%2 == 0 and z%2 != 0:
    print(max(x, z))
if x%2 == 0 and y%2 != 0 and z%2 != 0:
    print(max(y, z))
if x%2 != 0 and y%2 == 0 and z%2 == 0:
    print(x)
if x%2 == 0 and y%2 != 0 and z%2 == 0:
    print(y)
if x%2 == 0 and y%2 == 0 and z%2 != 0:
    print(z)
if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print(min(x, y, z))


#########################################
x, y = 2, 3
x, y = y, x
print('x =', x)
print('y =', y)

#########################################

'a'

3*4

3*'a'

3+4

'a'+'a'

'a'*'a'   # TypeError: can't multiply sequence by non-int of type 'str'


#########################################

len('abc')
len(12345678)   # TypeError: object of type 'int' has no len()
len('12345678')
len(1,2,3,4,5,6,7,8)  # TypeError: len() takes exactly one argument (8 given)

len[1,2,3,4,5,6,7,8]   # TypeError: 'builtin_function_or_method' object is not subscriptable

len{1,2,3,4,5,6,7,8}   # SyntaxError: invalid syntax

######################################################
'abc'[0] 
'abc'[2]

# Negative numbers are used to index from the end of a string.
'abc'[-1]   #   'c'
###########################################################

"""Slicing is used to extract substrings of arbitrary length. If s is a
string, the expression s[start:end] denotes the substring of s
that starts at index start and ends at index end-1."""

'abc'[1:3] #evaluates to 'bc'
"""If the value before the colon is
omitted, it defaults to 0. If the value after the colon is omitted, it
defaults to the length of the string."""

"""'abc'[:] is semantically equivalent to the more verbose
'abc'[0:len('abc')]."""   'abc'

'abc'[:]  # 'abc'

'123456789'[0:8:2]   # v'1357'

#####################################################

# Type conversions (also called type casts) 
"""It is often convenient to convert objects of other types to strings
using the str function"""

num = 30000000
fraction = 1/2
print(num*fraction, 'is', fraction*100, '%', 'of', num)
print(num*fraction, 'is', str(fraction*100) + '%', 'of',
num)
""" The first print statement inserts a space between 50 and % because
Python automatically inserts a space between the arguments to
print. The second print statement produces a more appropriate
output by combining the 50 and the % into a single argument of type
str."""
   
############################################################    

#LONG SYNTAX
x = 1111111111111111111111111111111 +\
222222222222333222222222 +\
3333333333333333333333333333333

print(x)
4444444666666666666777666666666

x = (1111111111111111111111111111111 +
222222222222333222222222 +
3333333333333333333333333333333)

print(x)
4444444666666666666777666666666

############################################################
# INPUT

n = input('Enter an int: ')
print(type(n))


n = input('Enter an int: ')
print(type(n))


##############################################################
##########   While Loops   ###################

num_x = int(input('How many times should I print the letter X? '))
to_print = num_x

print(to_print)

# concatenate X to to_print num_x times

print(to_print*'X')


#Find a positive integer that is divisible by both 11 and 12
x = 1
while True:
    if x%11 == 0 and x%12 == 0:
        break
    x = x + 1   # try this line without indent !!!
print(x, 'is divisible by 11 and 12')

################# EXERCISE ########################
"""Finger exercise: Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect."""

#####################################################

##############  For Loops and Range  ###########################

"""The general form of a for statement is (recall that the words in
italics are descriptions of what can appear, not actual code):
    
for variable in sequence:
code block

The variable following for is bound to the first value in the sequence,
and the code block is executed. The variable is then assigned the
second value in the sequence, and the code block is executed again.
The process continues until the sequence is exhausted or a break
statement is executed within the code block. For example, the code"""
total = 0
for num in (77, 11, 3):
    total = total + num
print(total)
#will print 91. The expression (77, 11, 3) is a tuple.

#######
"""The range function takes three integer arguments: start,
stop, and step. It produces the progression start, start + step,
start + 2*step, etc. If step is positive, the last element is the largest
integer such that (start + i*step) is strictly less than stop. If step is
negative, the last element is the smallest integer such that
(start + i*step) is greater than stop. For example, the expression
range(5, 40, 10) yields the sequence 5, 15, 25, 35, and the
expression range(40, 5, -10) yields the sequence 40, 30, 20, 10.
If the first argument to range is omitted, it defaults to 0, and if the
last argument (the step size) is omitted, it defaults to 1. For example,
range(0, 3) and range(3) both produce the sequence 0, 1, 2. The
numbers in the progression are generated on an “as needed” basis, so
even expressions such as range(1000000) consume little memory."""


x = 4
for i in range(x):
    print(i)


for i in range(2):   # When the sequence is exhausted, the loop terminates.
    print(i)
    i = 0
    print(i)

x = 1
for i in range(x):
    print(i)
    x = 4


######    nest loops

x = 4
for j in range(x):
    print(x,'j=',j)
    for k in range(x):
        print(x,'k=',k)
        x = 2
        
        
x = 3
for j in range(x):
    print('Iteration of outer loop')
    for i in range(x):
        print(' Iteration of inner loop')
        x = 2
        
###########   The for statement can be used in conjunction with the in
"""operator to conveniently iterate over characters of a string. For
example,"""

total = 0
for c in '12345678':
    total = total + int(c)
print(total)

"""sums the digits in the string denoted by the literal '12345678' and
prints the total."""

############### Finger exercise:                     ##################
"""Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside 
a for loop that iterates over the odd integers between 3 and 999."""
