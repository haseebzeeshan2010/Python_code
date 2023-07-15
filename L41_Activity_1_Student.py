# Create an empty list named numList
from os import remove


numList = []

# Append the numbers 20, 30, ... 100 to numList
#    Think about how to do this with a for loop
for i in range(20,100,10):
    numList.append(i)


# Display numList
print(numList)

# Display a separator on the screen
print("----------------------------------------------------")

# ---------------------------------------------------------
# Insert the number 10 at the front of numList
numList.insert(0,10)

# Insert the number 45 at the correct location
numList.insert(4,45)

# Insert the number 55 at the correct location
numList.insert(6,55)

# Insert another number 55 at the correct location
numList.insert(6,55)

# Display numList
print(numList)

# Display the length of numList
print(len(numList))

# Display a separator on the screen
print("----------------------------------------------------")

# ---------------------------------------------------------
# Display the number at the last position
print(numList[11])

# Replace the item at index 3 with 44
numList[3] == 44

# Display the list

print(numList)

# Display a separator on the screen
print("------------------------------------------------")

# ---------------------------------------------------------
# Use del to delete the item at index 3
del numList[3]

# Use .remove to remove the duplicate value 55
numList.remove(55)

# Display the list

print(numList)