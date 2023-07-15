INTEGERS = int(input("How many consecutive integers are there? "))
sum = float(input("What is the sum of the integers? "))
check = input("Consecutive odd,normal or even integers(o = odd, n = normal, e = even) ")
l=0
l1 = 0
l2=0
if check == "n":
    for x in range(INTEGERS):
        l=l+x
    the_sum = sum-INTEGERS
    total = (the_sum-l)/INTEGERS

    for r in range(INTEGERS):

        print(total+r+1)

elif check == "o":
    for x1 in range(INTEGERS):
        l1=l1+(x1*2)
        
    total1 = (sum-l1)/INTEGERS
    for r1 in range(INTEGERS):

        print(total1+r1)

elif check == "e":
    for x2 in range(INTEGERS):
        l2=l2+(x2*2)
        
    total2 = (sum-l2)/INTEGERS
    for r2 in range(INTEGERS):

        print(total2+(r2*2))