typecalculation = input("Do you want to calculate CSC,SEC,COT,SIN,COS,TAN: ")
hypotenuse = 0
opposite = 0
adjacent = 0
total = 0


def cosecant():
    hypotenuse = int(input("What is the hypotenuse length "))
    opposite = int(input("What is the opposite length "))
    total = hypotenuse/opposite
    return(total)

def secant():
    hypotenuse = int(input("What is the hypotenuse length "))
    adjacent = int(input("What is the adjacent length "))
    total = hypotenuse/adjacent
    return(total)

def cotangent():
    adjacent = int(input("What is the adjacent lenth "))
    opposite = int(input("What is the opposite length "))
    total = adjacent/opposite
    return(total)
def sin():
    opposite = int(input("What is the opposite length "))
    hypotenuse = int(input("What is the hypotenuse length "))
    total = opposite/hypotenuse
    return(total)
def cos():
    adjacent = int(input("What is the adjacent length "))
    hypotenuse = int(input("What is the adjacent length "))
    total = adjacent/hypotenuse
    return(total)
def tan():
    opposite = int(input("What is the opposite length "))
    adjacent = int(input("What is the adjacent length "))
    total = opposite/adjacent
    return(total)
if typecalculation == "CSC":
    value = cosecant()
    print(value)
elif typecalculation == "SEC":
    value = secant()
    print(value)
elif typecalculation == "COT":
    value = cotangent()
    print(value)
elif typecalculation == "SIN":
    value = sin()
    print(value)
elif typecalculation == "COS":
    value = cos()
    print(value)
else:
    value = tan()
    print(value)
