def printHeader():
    print("********************")
    print("*****Heading1*******")
    print("********************")


def underline(x):
    print(30*x)


def addPrint(p,q):
    summed = p+q
    print("Added value ",summed)


def addFunction(v1,v2):
    total = v1 + v2
    return total

printHeader()
underline("_")
underline("%")
addPrint(8,9)

sumTotal = addFunction(9,8)
print(sumTotal)