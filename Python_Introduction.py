#HELLO
#sign means text that follows is a comment, not code
#[CTRL+S] is shortcut to save a file
#[F5] is shortcut to run a file

print("Hello World 123")  #Use print() to output to the screen

#--------------------------------------------------------------
#DATATYPES
a=5             #setting the variable a equal to the number 5
b="January"     #setting the variable b equal to the string value "January" (Alpha numeric characters)
c=7.384         #setting the variable c equal to float value 7.384
d=True          #boolean
e="5"           #string

print(a)
print(type(a))

#NOW YOU
#We have done (a)
#Please write code here, for b,c,d

print(b) # continue from here...
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d))

print(e)
print(type(e))



#--------------------------------------
#CASTING
#casting an integer datatype as a string datatype (turning an integer into a string)
str_a = str(a) # str() casts an integer (or float) into a string 
print(str_a)
print(type(str_a))

#Casting a string datatype as an integer
int_e=int(e)
print(int_e)
print(type(int_e))

#---------------------------------------

name="Fred"  #name is a Variable, "Fred" is a String (of Characters)
print(name)

print("Hello" + " " + name) #concatenating strings

#input() statement
name2=input("What is your name? ") #input() allows user to enter data into the variable
print("Good to see you" + " " + name2)

#---------------------------------------
#setting a variable
x=7     #when you set a variable you use ONE equal sign (x equals 5)
y="OK"
print(x)
print(y)

a=x*y # we can multiply a string by an integer (we cannot add them)
print(a)

b=2*x #we can multiply integers (and floats)
print(b)

c="ABC" + " " + y #we can concatenate strings
print(c)

#--------------------------------------------
#IF ELSE
if 5>2:             #if statement ends with a :
    print("Yes")        #statements belonging to the if must all be indented four spaces
    print("It is")
else:               #else statement ends with a :
    print("No")         #statements belonging to the else must all be indented four spaces
    print("Of Course not")


ans_1=input("What is the capital of Italy? ")
if ans_1 == "Rome": #when you test a variable you use TWO equal signs (if x is equal to y?)
    print("Correct")
else:
    print("Incorrect")

#----------------------------------------------------
#INCORRECT CODE for numerical comparison
ans_1=input("What is 3+5 equal to? ")  
if ans_1 == 8: #this won't work because ans_1 is a string and 8 is an integer
    print("Correct")
else:
    print("Incorrect - logic error in code")

#CORRECT CODE for numerical comparison
ans_1=input("What is 3+5 equal to? ")
ans_1=int(ans_1) #int() turns string value into integer (error produced if user enters "A")
#ans_1=int(input("What is 3+5 equal to? "))
if ans_1 == 8:
    print("Correct")
else:
    print("Incorrect")

#-------------------------------------------------------
#IF ELIF ELSE
ans_1=input("What is the capital of England? ")
if ans_1 == "London": #when you test a variable you use TWO equal signs (if x is equal to y?)
    print("Correct")
elif ans_1 == "london": # you can have as many elif statements as you need e.g. if elif elif elif else
    print("Correct, but please spell proper nouns with a capital letter")
else:   # you can only have ONE else statement  (only ONE if statement also of course)
    print("Incorrect")

#--------------------------------------------------------
#NOW YOU
#Write three or more quiz questions of your own here
#When you are happy they work copy them into a new file called Quiz_v1.py or similar

#ans_2 = input("Approximately one quarter of human bones are in the feet. True or False")
#if ans_2 == "True" or "true":
#    print("Correct")
#else:
#    print("Incorrect, The correct answer is True, one quarter of human bones are in the feet.")

#ans_3 = input("The total surface area of a human lungs is the size of a football pitch. True or False")
#if ans_3 == "True" or "true":
#    print("Correct")
#else:
#    print("Incorrect, The correct answer is True, the surface area of human lungs is the size of a football pitch")

#ans_4 = input("The loudest animal is the African Elephant.")
#if ans_4 == "True" or "true":
#    print("Incorrect, the loudest animal is the sperm whale")
#else:
#    print("Correct")





#--------------------------------------------------

#MORE NOW YOU#
# Please make output user friendly. E.g. "The Sum is: 5"

#--------------------------
#1 Write a program that takes in two numbers and outputs the sum
num_1=int(input("Please enter first number: "))
num_2=int(input("Please enter second number: "))
theSum = num_1 + num_2
print("The sum is: " + str(theSum)) #why have we put str() around theSum?

#--------------------
#2 Write a program that takes in two numbers and outputs the larger one



#-------------------
#3 Write a program that takes in three numbers and outputs the average



    


