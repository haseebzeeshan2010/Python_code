# myString = input("Please enter the text ")

# for i in range(len(myString)):
#     number = ord(myString[i])
#     print(number)


myString = ""

for index in range(0,10):
    number = int(input("Enter a number: "))
    character = chr(number)
    myString = myString+character