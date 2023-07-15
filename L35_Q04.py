word = input ("Enter a word: ")

# Complete the presence check
if (word == ""):
    print ("Word cannot be blank")

# Complete the length check
elif (len(word)<=5):
    print ("Word not long enough")
else:
    print ("Valid word")

number = int (input ("Enter an integer: "))

# Complete the range check
if not((number>=10)and(number<=50)):
    print ("Invalid number")
else:
    print ("Valid number")