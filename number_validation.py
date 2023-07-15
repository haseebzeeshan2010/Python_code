number = input("Please enter a number from 0-10 ")

if number.isdigit() == False:
    print("Invalid entry")
elif int(number) > 10:
    print("Invalid entry")
elif int(number) < 0:
    print("Invalid entry")
else:
    number = int(number)
    if number == 5:
        print(f"You entered {number}")
    elif number == 0:
        exit()
    elif number < 5:
        print(f"You entered a {number}, which is less than 5")
    else:
        print(f"You entered a {number}, which is more than 5")