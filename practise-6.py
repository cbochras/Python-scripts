# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 21:20:43 2021

"""

###############  Files      ###################
"""Python provides many facilities for creating
and accessing files. Here we illustrate some of the basic ones.
Each operating system (e.g., Windows and macOS) comes with
its own file system for creating and accessing files. Python achieves
operating-system independence by accessing files through something
called a file handle. The code
name_handle = open('kids', 'w')
instructs the operating system to create a file with the name kids and
return a file handle for that file. The argument 'w' to open indicates
that the file is to be opened for writing. The following code opens a
file, uses the write method to write two lines. (In a Python string, the
escape character “\” is used to indicate that the next character should
be treated in a special way. In this example, the string '\n' indicates
a newline character.) Finally, the code closes the file. Remember
to close a file when the program is finished using it. Otherwise there
is a risk that some or all of the writes may not be saved."""

"""Python provides many facilities for creating
and accessing files. Here we illustrate some of the basic ones.
Each operating system (e.g., Windows and macOS) comes with
its own file system for creating and accessing files. Python achieves
operating-system independence by accessing files through something
called a file handle. The code"""

name_handle = open('kids', 'w')
print(name_handle)
#prints:
 # <_io.TextIOWrapper name='kids' mode='w' encoding='cp1254'>

"""instructs the operating system to create a file with the name kids and
return a file handle for that file. The argument 'w' to open indicates
that the file is to be opened for writing. The following code opens a
file, uses the write method to write two lines. (In a Python string, the
escape character “\” is used to indicate that the next character should
be treated in a special way. In this example, the string '\n' indicates
a newline character.) Finally, the code closes the file. Remember
to close a file when the program is finished using it. Otherwise there
is a risk that some or all of the writes may not be saved."""


name_handle = open('kids', 'w')
for i in range(2):
    name = input('Enter name: ')  
    name_handle.write(name + '\n') #
name_handle.close()

# suppose that in first iteration name is Ahmet, in second iteration
# name is Mehmet, then, 'kids' contains 2 lines when opened by Notepad:
# Ahmet
# Mehmet

#######  OPEN A FILE  IN PYTHON   ############

with open('kids', 'r') as name_handle: #OR use name_handle = open('kids', 'r')
    for line in name_handle:
        print(line)
 #prints?
 
Ahmet

Mehmet       
        
name_handle = open('kids2', 'w')
for i in range(2):
    name = input('Enter name: ')  
    name_handle.write(name)    # without   \n  (newline)
name_handle.close()

with open('kids2', 'r') as name_handle:
    for line in name_handle:
        print(line)
 #prints:
#     ZeynepAylin    no space between 2 names

#   OR
name_handle = open('kids', 'w')
name_handle.write('Michael')
name_handle.write('Mark')
name_handle.close()
name_handle = open('kids', 'r')
for line in name_handle:
    print(line)    # MichaelMark
    
######    APPEND ###########
""" If we don't want to overwrite onto previous contents, use 'append' """

name_handle = open('kids', 'a')
name_handle.write('David')   
name_handle = open('kids', 'r')
for line in name_handle:
    print(line)    #  MichaelMarkDavid


####  OTHER COMMON FILE OPERATORS   ########

myFile_hndl = open('myFile', 'w')
myFile_hndl.write('Ali'+'\n')
myFile_hndl.write('Ahmet'+'\n')
myFile_hndl.write('Mehmet')
myFile_hndl.close()

with open('myFile', 'r') as f:
    print(f.readlines())  # reads all lines including '\n'
    
    #prints: ['Ali\n', 'Ahmet\n', 'Mehmet']

# If we want to remove the white space characters like '\n'

with open('myFile') as f:
    lines = [line.rstrip() for line in f]
print(lines)    #  ['Ali', 'Ahmet', 'Mehmet']

# also 
with open('myFile') as f:
    print(f.read().splitlines())   #   ['Ali', 'Ahmet', 'Mehmet']
    
    
 with open('myFile', 'r') as f:
    print(f.readline())  #    reads only Ali
    

with open('myFile2', 'w') as f:
    f.writelines(['Ayşe\n', 'Hatice\n', 'Elif'])
    f.close()    
        
with open('myFile2', 'r') as f:    
    print(f.read().splitlines())   #  ['Ayşe', 'Hatice', 'Elif']
    
    
    
    
    
    
myFile_hndl = open('myFile', 'w')
myFile_hndl.write('Ali'+'\n'+'Ahmet'+'\n'+'Mehmet')
# myFile_hndl.write('Ahmet'+'\n')
# myFile_hndl.write('Mehmet')
myFile_hndl.close()
myFile_hndl = open('myFile', 'r')    
for line in myFile_hndl:
    print(line) 
    print(myFile_hndl.readline())
myFile_hndl.close()
    
    
