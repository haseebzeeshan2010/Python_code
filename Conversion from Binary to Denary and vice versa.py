print("""
     _____________________
    |  _________________  |
    | | 1100 = 12       | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
""")

conversion_type = input("Do you want to convert Denary to Binary or Binary to Denary (Write DB for denary to binary and BD for binary to denary)")
output = []
indices = 0
answer = ""
total = 0
switch = []



if conversion_type == "DB": 
    number = int(input("Please enter the number which you want to convert: "))
    if number > 0:    
        while number != 0:

            if number % 2 == 0:
                number=number/2
                output.insert(0,0)
            else:
                number=(number-1)/2
                output.insert(0,1)

        for string in output:
            answer = answer+str(string)
    else:
        answer = 0

    print(f"The binary answer is {answer}")

elif conversion_type == "BD":
    number = input("Please enter the number which you want to convert: ")

    for b in number:
        switch.insert(0,int(b))

    for binary in switch:

        if binary == 1:
            output.append(2**indices)
            indices+=1
        else:
            indices+=1
    for add in output:
        total += add
        
    print(f"The Denary number is {total}")
