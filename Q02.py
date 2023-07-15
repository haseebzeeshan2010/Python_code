# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# ===>  Change the identifier x to a more meaningful name
sing = ""
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# ===> Display a suitable question to the user
sing = input("Would you like me to sing? (y/n)")
# ===> Accept the user's input (no validation required)

if (sing == 'y'):
    # ===> Add a comment to explain the effect of the last -1 in this call
    for num in range(5, -1, -1):
        print (num, "green bottles sitting on the wall")
print ("Goodbye")
