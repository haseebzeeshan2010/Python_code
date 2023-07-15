# ----- Global variables -----
architects = [["Hadid", "Zaha", 1950, 2016],
              ["Lin", "Maya", 1951, 0],
              ["Decq", "Odile", 1955, 0],
              ["Griffin", "Marion", 1871, 1961]]


# ----- Subprograms -----
def addKeys ():
    # =====> Write your code here
    for i in range(0,len(architects)):
        record = architects[i]

        lastname = record[0]
        firstletter = record[1][0]
        birthyear = str(record[2])

        key = lastname+firstletter+birthyear
        
        architects[i].append(key)


# ----- Main program -----
addKeys ()

print (architects)
print ("Goodbye")