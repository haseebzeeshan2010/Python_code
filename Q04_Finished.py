#Define the function
def trapezium_calculate():
    #Take the inputs from the user and store them in a variable as a float
    width = float(input("What is the width of the trapezium "))
    base = float(input("What is the base length of the trapezium "))
    height = float(input("What is the height of the trapezium ")) 
    #Do the calculations   
    calculate = (1/2)*(width+base)*height
    #Round the answer
    return(round(calculate,2))

#Call the function and print the answer
print(f"The area of the trapezium is: {trapezium_calculate()}")


