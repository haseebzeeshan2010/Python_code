# -------- Lesson 1 -------

# ------- Syntax errors -------
#An example of a syntax error is:

#print("Hello, how are you"}

# syntax errors are when you break a rule in the programming language, if you run this, you will get a syntax error
# The right code will be:

print("Hello, how are you")

# ------ Variables --------

# A variable can be written like:
value = 1
# Variables are basically virtual boxes, the only difference is that they can store values rather than items

# -- Aditional information about variables --

# They can hold values other than numbers, like:

value = 'Hi' # This is known as a string
value = True # This is known as a boolean

# Just make sure you know the difference between integers and floats!

value = 1 # <-- This is an integer, it doesn't have any decimal as its value(numbers without a decimal but with a minus sign are still integers), if it had a value like 1.1 , which has a decimal, then it would be a float
value = 1.1 # <-- This is a float, it has a decimal value unlike an integer, it also uses more memory than an integer

# ------ Arithmetic Operators ------

# Arithmetic operators are used to do calculations in python, you most likely use them in everyday life, here are some examples:


print(9*(2+1)) # The first operator to know about is the bracket it is used to do calculations like in maths, like 9*(2+1)
print(9**2) # the second operator is the power(indices) operator, it's the ** sign
print(5//3) # the third operator is the integer division operator, it's the // sign
print(5%3) # the fourth operator is the modulus operator(it outputs the whole number remainder after division), it's the % sign
print(10/5) # the fith operator is the division operator, it's the / sign
print(10*2) # the sixth operator is the multiplication operator, it's the * sign
print(7+5) # the seventh operator is the addition operator, it's the + sign
print(9-3) # the eighth operator is the subtraction operator, it's the - sign

# --------Data types---------

# All values in python are data types, there are 4 different data types

print(1) #Integers, basically whole numbers
print(1.1) #Floats, numbers with a decimal, you can use them to store whole numbers as well, but they use up more memory
print(True) #Boolean, True and False
print("What day is it today?") #Strings, just text, like 'Hi how are you'


# ------ Integrated Development Environment (IDE) ------

# This is what runs your code, you use it to:

# type in program code
# save it into a file on disk
# identify and correct errors
# execute (run) the code
# input data through the keyboard (if required)
# view output displayed on the screen (if there is any).

# When you make a program, you normally follow and repeat these steps to make a program:

#Step 1: Open the integrated development environment

#Step 2: Load a program code file

#Step 3: Examine for syntax errors

#Step 4: Correct the syntax errors

#Step 5: Run the code

#Step 6: Review the program output, and make sure to save it, in case your IDE doesn't save itself

# ---- Task ----

# Make and fix your first program

# Step 1

# Open the IDE

# Step 2

#Load the file you need to fix, this code is from lesson 1 Core content 2 in the platform, link : 
# https://pearsononlineacademyukg.lms.pearsonconnexus.com/student/28407390/activity/f541576874d94531bf6410aa9f5612df

# firstName = "Chunhua
# numCars = 48
# side = 5
# heightMetres  1.5
# tax = 0.20
# isSummer = True
# print (42 // 10)
# print 42 % 10)
# print (5 ** 2)
# print (9 + 3 * 8)
# print ((9 + 2) * 8)
# print (firstName
# print (numCars + heightMetres)
# print (tax * side)
# print (123isSummer)

# # Step 3

# # The wavy red lines show where a syntax error occurs in the code. There is an error in the grammar of the statement. 
# # Place the mouse over one of the red squiggly lines and a tool tip should appear. Sometimes, this tooltip will advise 
# # how to fix the error. Sometimes, the syntax analyser cannot solve it. Nevertheless, there is an error on or near that 
# # line.

# # Step 4

# # Fix the code

# # First try figuring it out yourself, and then look at the solution



# #Here is the corrected code:

# firstName = “Chunhua”

# numCars = 48

# side = 5

# heightMetres = 1.5

# tax = 0.20

# isSummer = True

# print (42 // 10)

# print (42 % 10)

# print (5 ** 2)

# print (9 + 3 * 8)

# print ((9 + 2) * 8)

# print (firstName)

# print (numCars + heightMetres)

# print (tax * side)

# print (isSummer)


#Line 1 needs another double quote at the end.

#Line 4 needs an assignment operator ‘=’.

#Line 8 needs an opening bracket before the number 42.

#Line 12 needs a closing bracket, at the end of the line.

#Line 15 needs the ‘123’ deleted, because variable names cannot start with a number.

# Step 5

# Run the code in your IDE

# Step 6

# Review the output, an exit code of 0 means there was no error

# Great job, you made the first program of the course