age = int(input("Enter your age: "))

if(age<1) or (age>110):
    print("Try again")
    if(age >= 5) and (age<=19):
        print("Go to school")
    else:
        print("Have a lovely day")