import random
print("""

    _______            
  /\       \           
 /()\   ()  \          
/    \_______\         
\    /()     /         
 \()/   ()  /          
  \/_____()/



                    """)
dice_amount = int(input("Welcome to the dice roller!, how many dice do you want to roll? "))
dice_rolls = []
loop = True
while loop is True:
    for i in range(dice_amount):
        dice_rolls.append(random.randint(1,6))

    for l in dice_rolls:
        
        if l == 1:  
            print(f"You rolled a {l}!")   
            print("""

             __________
            |          |
            |          |
            |    ()    |
            |          |
            |__________|
            
                
                                """)
            

        elif l == 2 :
            print(f"You rolled a {l}!")
            print("""

             __________
            |          |
            |  ()      |
            |          |
            |      ()  |
            |__________|
            
    
                        """)
            
            

        elif l == 3 :
            print(f"You rolled a {l}!")
            print("""

             __________
            |          |
            |  ()      |
            |    ()    |
            |      ()  |
            |__________|
            
                
                        """)
            

        elif l == 4 :
            print(f"You rolled a {l}!")
            print("""

             __________
            |          |
            | ()    () |
            |          |
            | ()    () |
            |__________|
            
                
                        """)


        elif l == 5 :
            print(f"You rolled a {l}!")
            print("""

             __________
            |          |
            | ()    () |
            |    ()    |
            | ()    () |
            |__________|
            
                
                        """)

        elif l == 6 :
            print(f"You rolled a {l}!")
            print("""

             __________
            |          |
            | ()    () |
            | ()    () |
            | ()    () |
            |__________|
            
                
                        """)
    check = input("Do you want to roll again? (Yes or No) ")
    if check == "Yes" or check == "yes":
        loop = True
        dice_rolls = []
        print("-------------------------------------------")
    else:
        loop = False
        dice_rolls = []
        print("-----------------Ended---------------------")
        