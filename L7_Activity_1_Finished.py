#Initializing constant
PI = 3.14159

#Asking user for radius input
radius = int(input("Enter the radius "))

#Doing the calculation 2πr
calculate = 2*PI*radius

#Rounding of the answer
rounded = round(calculate,3)

#Displaying the answer
print("The circumference is ",rounded)