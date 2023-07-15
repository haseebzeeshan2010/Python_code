#Things to as from Sir:
#Rule 7 of card deck
#Improvements
#A flowchart

import random

p1_cards=[]
p2_cards=[]
player1_totalcards = []
player2_totalcards = []
authenticator = []



sign_in = input("Do you want to register(Y or N) ")


def register():
    username_new = input("What is the username of your account? ")
    password_new = input("What is the password of your account? ")
    userdata_append = open('userdata.csv',"a")
    userdata_append.write("\n"+username_new+","+password_new+",")
    userdata_append.close

def login():
    username_input = input("Please enter your username ")
    password_input = input("Please enter your password ")
    for row in userdata:
        row_username = row.split(",")[0]
        row_password = row.split(",")[1]
        if row_password == password_input and row_username == username_input:
            authenticator.append("True")

userdata = open('userdata.csv',"r+")

if sign_in == "N":
    login()
    # for row in userdata:
    #     row_username = row.split(",")[0]
    #     row_password = row.split(",")[1]
    #     if row_password == password_input and row_username == username_input: # == "" and row.split(",")[1] == "":
    #         authenticator.append("True")
        

    if len(authenticator) > 0:
            

        def p1_gets_cards(card1,card2):
            p1_cards.append(card1)
            p1_cards.append(card2)
            print("player 1's cards",player1_totalcards)

        def p2_gets_cards(card1,card2):
            p2_cards.append(card1)
            p2_cards.append(card2)
            print("player 1's cards",player1_totalcards)
            
        def ShuffleDeck():
            shuffledDeck=[]
            #print("shuffledDeck",shuffledDeck)
            orderedDeck=["R 1","R 2","R 3","R 4","R 5","R 6","R 7","R 8","R 9","R 10","Y 1","Y 2","Y 3","Y 4","Y 5","Y 6","Y 7","Y 8","Y 9","Y 10","B 1","B 2","B 3","B 4","B 5","B 6","B 7","B 8","B 9","B 10"]
            #print("orderedDeck",orderedDeck)
            orderedDeckLen=len(orderedDeck)

            for i in range(0,orderedDeckLen):
                #print("")
                orderedDeckLen=len(orderedDeck)
                #print("orderedDeckLen",orderedDeckLen)
                #print("orderedDeck",orderedDeck)

                randInt=random.randint(0, orderedDeckLen-1)
                #print("randInt",randInt)

                card=(orderedDeck[randInt])
                #print("card",card)

                shuffledDeck.append(card)
                #print()
                #print("******************************************")
                #print("shuffledDeck",shuffledDeck)
                #print("******************************************")
                    
                orderedDeck.pop(randInt)


        
            #print("End of deck shuffle---------------------------------------")
            #print()
            return shuffledDeck
        
        def playGame(shuffledDeck):
            while len(shuffledDeck)>0:
                #player1 picks first card and player2 picks second card from the shuffled deck
                player1_totalcards.append(shuffledDeck[0].replace(" ",""))
                player2_totalcards.append(shuffledDeck[1].replace(" ",""))
                p1_card=shuffledDeck[0].split()
                p2_card=shuffledDeck[1].split()

                print("player 1's card is ",player1_totalcards[0])
                print("player 2's_card is ",player2_totalcards[0])
                print("")
                p1_card_colour=p1_card[0]
                p2_card_colour=p2_card[0]

                p1_card_number=p1_card[1]
                p2_card_number=p2_card[1]

                if int(p2_card_number)!=10:
                    p2_card_number+=" "
                else:
                    p2_card_number = p2_card_number
                
                if int(p1_card_number)!=10:
                    p1_card_number+=" "
                else:
                    p2_card_number = p2_card_number        



                if p1_card_colour==p2_card_colour:
                    print("The card colour is the same, compare card number")
                    print("")
                    
                    print("player1's card number: ",p1_card_number)
                    
                    print("player 2's card number: ",p2_card_number)
                        

                    print("")
                    print(f"""Player 1 got:                                Player 2 got:
                        ___________                                  ___________
                        |           |                                |           |
                        | {p1_card_number}        |                                | {p2_card_number}        |
                        |           |                                |           |
                        |     {p1_card_colour}     |                                |     {p2_card_colour}     |     
                        |           |                                |           |
                        |        {p1_card_number} |                                |        {p2_card_number} |         
                        |___________|                                |___________|
                
                """)


                    if p1_card_number > p2_card_number:
                        print("")
                        print ("player 1's card number is less than player 2's card number")
                        print("")
                        p1_gets_cards(p1_card, p2_card)
                    else:
                        print ("p1 card number is greater than p2 card number")
                        p2_gets_cards(p1_card, p2_card)

                else:

                    if p1_card_colour=="R":
                        print("")
                        print(f"""Player 1 got:                                Player 2 got:
                        ___________                                  ___________
                        |           |                                |           |
                        | {p1_card_number}        |                                | {p2_card_number}        |
                        |           |                                |           |
                        |     {p1_card_colour}     |                                |     {p2_card_colour}     |     
                        |           |                                |           |
                        |        {p1_card_number} |                                |        {p2_card_number} |         
                        |___________|                                |___________|
                
                            """)
                        print("")
                        if p2_card_colour=="B":
                            p1_gets_cards(p1_card, p2_card)#player1 wins
                            print("Red beats black")

                            
                        else:
                            p2_gets_cards(p1_card, p2_card)#player2 wins
                            print("Red loses to yellow")

                    if p1_card_colour=="Y":
                        print("")
                        print(f"""Player 1 got:                                Player 2 got:
                        ___________                                  ___________
                        |           |                                |           |
                        | {p1_card_number}        |                                | {p2_card_number}        |
                        |           |                                |           |
                        |     {p1_card_colour}     |                                |     {p2_card_colour}     |     
                        |           |                                |           |
                        |        {p1_card_number} |                                |        {p2_card_number} |         
                        |___________|                                |___________|
                
                            """)
                        print("")                
                        if p2_card_colour=="R":
                            p1_gets_cards(p1_card, p2_card)#player1 wins
                            print("Yellow beats red")
                        else:
                            p2_gets_cards(p1_card, p2_card)#player2 wins
                            print("Yellow loses to black")

                    if p1_card_colour=="B":
                        print("")
                        print(f"""Player 1 got:                                Player 2 got:
                        ___________                                  ___________
                        |           |                                |           |
                        | {p1_card_number}        |                                | {p2_card_number}        |
                        |           |                                |           |
                        |     {p1_card_colour}     |                                |     {p2_card_colour}     |     
                        |           |                                |           |
                        |        {p1_card_number} |                                |        {p2_card_number} |         
                        |___________|                                |___________|
                
                            """)
                        print("")
                        if p2_card_colour=="Y":
                            p1_gets_cards(p1_card, p2_card)#player1 wins
                            print("Black beats yellow")
                        else:
                            p2_gets_cards(p1_card, p2_card)#player2 wins
                            print("Black loses to red")

                shuffledDeck.pop(0)
                shuffledDeck.pop(0)
                
                #print("----------shuffledDeck",shuffledDeck)
                print()
                print("Please press enter to continue.")
                input()

        def printWinner():
            print()
            print("--------------------------")
            print('final p1_cards',player1_totalcards)
            print('final p2_cards',player2_totalcards)

            if len(p1_cards)==len(p2_cards):
                print("Draw")
            else:
                if len(p1_cards)>len(p2_cards):
                    print("Player 1 wins")
                else:
                    print("Player 2 wins")

        #### MAIN ####
        shuffledDeck=ShuffleDeck()
        playGame(shuffledDeck)
        printWinner()
    else:
        print("Incorrect username or password")
else:
    register()