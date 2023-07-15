#L19 - Activity 2

quote="Computer science is my favourite subject."
print(quote)

firstName=input("Please enter your name (4 chars min): ")
print("Hello", firstName)

nameLength=len(firstName)
print("nameLength", nameLength)

if nameLength<4:
    print("Name to short")
else:
    print("Hello", firstName)

firstChar=firstName[0].upper()
print("firstChar", firstChar)

lastChar=firstName[nameLength-1:nameLength].upper()
print("lastChar", lastChar)
input()




number=input("Please enter a number between 1 and 10 inclusive: ")
print("number is: ",number)
print("data type is:", type(number))

number=int(number)
print("number is: ",number)
print("data type is:", type(number))

if number <1 or number >10:
    print("Number out of range")
else:
    print("good to go")


