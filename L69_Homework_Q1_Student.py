
# ----- Global variables -----
architects = [["Hadid", "Zaha", 1950, 2016],
              ["Lin", "Maya", 1951, 0],
              ["Decq", "Odile", 1955, 0],
              ["Griffin", "Marion", 1871, 1961]]


# ----- Subprograms -----
def addRecord ():

    # Get last name, first name, birth year, and death year
    firstname = input("What is the first name of the architect? ")
    lastname = input("What is the last name of the architect? ")
    birthyear = int(input("What is the birth year of the architect? "))
    deathyear = int(input("What is the death year of the architect? "))
    # Make a new record with the input values

    record = [lastname,firstname, birthyear, deathyear]


    # Add the record to the table
    architects.append(record)

# ----- Main program -----



addRecord()

print (architects)
print ("Goodbye")