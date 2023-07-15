
# ----- Global variables -----
architects = [["HadidZ1950", "Hadid", "Zaha", 1950, 2016],
              ["LinM1951", "Lin", "Maya", 1951, 0],
              ["DecqO1955", "Decq", "Odile", 1955, 0],
              ["GriffinM1871", "Griffin", "Marion", 1871, 1961]]


# ----- Subprograms -----
def displayAll (pList):
    # =====> Write your code here
    layout = "{:<16} {:<12} {:<12} {:^5} {:^5}"

    print (layout.format ("Key", "Last name", "First name", "Birth", "Death"))
    print ("-"*60)

    for record in pList:
        if (record[4] == 0):
            print (layout.format (record[0], record[1], record[2],
                                  record[3], ""))
        else:
            print (layout.format (record[0], record[1], record[2],
                                  record[3], record[4]))

# ----- Main program -----
displayAll (architects)