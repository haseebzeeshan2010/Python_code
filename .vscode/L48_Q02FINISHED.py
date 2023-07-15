print("Enter a number:")
number = int(input(""))
total = 0
count = 0

while number != 0:
    print("Enter a number:")
    number = int(input(""))
    total+=number
    count+=1


mean = total/count
print(count)
print(total)
print(mean)
