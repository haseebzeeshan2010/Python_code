#Syntax 1

#####################################################
#Declare Variables
a="ABC"     #string
b="DEF"     #string
x=5         #int
y=7         #int
p="5"       #string
q="7"       #string

#----------------------------------------------------
#Adding strings
print("")               #print(empty line)
var1=a+b                #string + string ==> concatenation
print(var1)             #print result on its own
print("var1 =",var1)    #print("Text", value)
print("-------------")  #print underline
               
#----------------------------------------------------
#Multiplying a string by an integer
print("")               #print(empty line)
var2=a*x                #string times integer
print("var2 is:",var2)  #print("Text", value)

#----------------------------------------------------
#Adding two integers
print("")               #print(empty line)
var3=x+y                #add the two integers
print("var3 is:",var3)  #print("Text", value)

#----------------------------------------------------
#Adding strings which look like numbers
print("")               #print(empty line)
var4=p+q                #string + string  "5" plus "7"
print("var4 =",var4)    #print("Text", value)
print("-------------")  #print underline

#----------------------------------------------------
#the input() statement
name=input("Please enter your name: ")  #input() - puts data entered by user into variable
print("Your name is:", name)
print("")                               #print(empty line)
age=input("Please enter your age: ")
print("Your age is:", age)
print("The datatype of the variable age is: ", type(age))

#----------------------------------------------------
#Adding two numbers input by user:
print("")                                   #print(empty line)
num1=input("Please enter first number: ")   #input() - puts data entered by user into variable
num2=input("Please enter second number: ")
num3= num1+num2
print("Adding the numbers input gives:",num3)  # adding strings

#turning numbers from string data type to integer datatype
print("Before conversion from string to int num1 is dataype", type(num1))
num1=int(num1)  #int() converts string to integer
print("")                                   #print(empty line)
print("num1=int(num1) turns datatype from string into integer")
print("After conversion from string to int num1 is dataype", type(num1))
print("now we can add num1 and num2 after int() conversion")
num2=int(num2)
num3= num1+num2
print("Adding the numbers now gives:",num3)  # adding integers

#----------------------------------------------------
#We can combine the input() and int() statemnts into one line.
print("")                                   #print(empty line)
num4=int(input("Please enter a number: "))
print("The value entered was:",num4, "and is now of datatype:", type(num4))

#Program to multiply two numbers:
num5=input("Please enter first number: ")   #num5 is string
num5=int(num5)                              #num5 converted to int
num6=int(input("Please enter first number: ")) #input and int conversion done in one line
num7=num5*num6

############################  NOW YOU ########################
#1. Write a program that:
#   Asks the user to input two numbers
#   Divides the first number by the second
#   Outputs the answer in format [The answer is value]

#2. Write a program that:
#   Asks the user to input two numbers
#   Raises the first number to the power of the second
#   Outputs the answer in format [num1 to the power of num2 is value]
#       e.g. 2 to the power of 3 is 8

#3. Write a program that:
#   Asks the user to input two numbers
#   Raises the first number to the power of the second
#   Outputs the answer in format [num1 to the power of num2 is value]
#       e.g. 2 to the power of 3 is 8

#4. Write a program that:
#   Asks the user to input two numbers
#   Calculates integer division of the first number by the second (floor division)
#   Outputs the answer as [X goes in to Y, Z times]

#5. Write a program that:
#   Asks the user to input two numbers
#   Gives the remainder of dividing the first number by the second (modulus)
#   Outputs the answer as [X divided by Y, gives a remainder of Z]

#6. Write a program that:
#   Asks the user to input their first name and surname.
#   Outputs the message ["Hello first name surname, hope you are well."]



