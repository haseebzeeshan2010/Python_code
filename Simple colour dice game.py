import random
stop = False
ask = False
lightblue = 4
darkblue = 4
orange = 4
yellow = 4
pink = 3
teal = 2
continuer = "Y"


while stop == False:
    '''
    dice_colour = random.randint(1,6)

    if dice_colour == 1 and lightblue != 4:
        print("lightblue")
        print("""

             ___________
            |           |
            |           |
            | lightblue |
            |           |
            |___________|
            
    
                        """)


        if lightblue < 4:
            lightblue += 1
            ask = False
        else:
            ask = False
    elif dice_colour == 2 and darkblue != 4:
        print("darkblue")
        print("""

             __________
            |          |
            |          |
            | darkblue |
            |          |
            |__________|
            
    
                        """)
        if darkblue < 4:
            darkblue += 1
            ask = True
        else:
            ask = False
    elif dice_colour == 3 and orange != 4:
        print("orange")
        print("""

             __________
            |          |
            |          |
            |  orange  |
            |          |
            |__________|
            
    
                        """)
        if orange < 4:
            orange += 1
            ask = True
        else:
            ask = False
    elif dice_colour == 4 and pink != 4:
        print("pink")
        print("""

             __________
            |          |
            |          |
            |   pink   |
            |          |
            |__________|
            
    
                        """)
        if pink < 4:
            pink += 1
            ask = True
        else: 
            ask = False
    elif dice_colour == 5 and teal != 4:
        print("teal")
        print("""

             __________
            |          |
            |          |
            |   teal   |
            |          |
            |__________|
            
    
                        """)
        if teal < 4:
            teal += 1
            ask = True
        else:
            ask = False
    elif dice_colour == 6 and yellow != 4:
        print("yellow")
        print("""

             __________
            |          |
            |          |
            |  yellow  |
            |          |
            |__________|
            
    
                        """)
        if yellow < 4:
            yellow += 1
            ask = True
        else:
            
            ask = False
    '''
    if ask == True:
        continuer = input("Continue? (Y or N)?").upper()

        if continuer == "Y":
            stop == False
        elif continuer =="N":
            stop == True
        else:
            print()
    else:
        print()
print("Goodbye")