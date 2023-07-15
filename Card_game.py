# Import random library
import random

# ASCII art for welcome
print("""

  ___   ___   ___   ___   ___   ___ 
 |A  | |2  | |3  | |4  | |5  | |6  |
 | /\| | /\| | /\| | /\| | /\| | /\|
 |_\/| |_\/| |_\/| |_\/| |_\/| |_\/|


""")


print("Welcome to the card game(R = Red, Y = Yellow, B = Black)")




# Initialize all the arrays and variables that are going to be used

ordered_deck = ["R 1","R 2","R 3","R 4","R 5","R 6","R 7","R 8","R 9","R 10","Y 1","Y 2","Y 3","Y 4","Y 5","Y 6","Y 7","Y 8","Y 9","Y 10","B 1","B 2","B 3","B 4","B 5","B 6","B 7","B 8","B 9","B 10"]
shuffled_deck = []
pick = True
player1_counter = 0
player2_counter = 0

#Players' arrays

player1 = []
player2 = []

#Initializing the variables that will help calculate the index that will be taken from the array

randomnum_player1 = 0
randomnum_player2 = 0

#Initializing card variable to the length of the ordered_deck array

cards = len(ordered_deck)

#Shuffler for ordered_deck

for shuffle in ordered_deck:
    shuffled_deck.insert(random.randint(0,30),shuffle)

#While loop to check if all the cards haven't been taken

while cards != 0:

    #calculations for player1's card and number

    randomnum_player1 = random.randint(0,len(shuffled_deck)-1)
    player1.append(shuffled_deck[randomnum_player1])
    player1_process = shuffled_deck[randomnum_player1].split()
    shuffled_deck.pop(randomnum_player1)


    #calculations for player2's card and number

    randomnum_player2 = random.randint(0,len(shuffled_deck)-1)
    player2.append(shuffled_deck[randomnum_player2])
    player2_process = shuffled_deck[randomnum_player2].split()
    shuffled_deck.pop(randomnum_player2)
    
    
    # Player1's number and colour of the current card
    player1_colour = player1_process[0]
    player1_number = player1_process[1]

    # Player2's number and colour of the current card
    player2_colour = player2_process[0]
    player2_number = player2_process[1]


#To make it so that when the card number is double digits, then it doesn't make the ASCII card have a space
    if int(player1_number) >=10:
        player1_number_card = player1_number
    else:
        player1_number_card = player1_number+" "


    if int(player2_number) >=10:
        player2_number_card = player2_number
    else:
        player2_number_card = player2_number+" "


#Conditionals for the card colours and numbers

    if player1_colour == "R" and player2_colour == "B":
        #A counter which increases when the player wins a round, this is used to calculate the winner
        player1_counter += 1
        #Card interpolation
        print(f"""Player 1 got:                                Player 2 got:
                 ___________                                  ___________
                |           |                                |           |
                | {player1_number_card}        |                                | {player2_number_card}        |
                |           |                                |           |
                |     {player1_colour}     |                                |     {player2_colour}     |     
                |           |                                |           |
                |        {player1_number_card} |                                |        {player2_number_card} |         
                |___________|                                |___________|
        
        """)
        
        print("Player 1 won this round")
    elif player2_colour == "R" and player1_colour == "B":
        player2_counter += 1

        print(f"""Player 1 got:                                Player 2 got:
                 ___________                                  ___________
                |           |                                |           |
                | {player1_number_card}        |                                | {player2_number_card}        |
                |           |                                |           |
                |     {player1_colour}     |                                |     {player2_colour}     |     
                |           |                                |           |
                |        {player1_number_card} |                                |        {player2_number_card} |         
                |___________|                                |___________|
        
        """)

        print("Player 2 won this round")
    elif player1_colour == "Y" and player2_colour == "R":
        player1_counter += 1

        print(f"""Player 1 got:                                Player 2 got:
                 ___________                                  ___________
                |           |                                |           |
                | {player1_number_card}        |                                | {player2_number_card}        |
                |           |                                |           |
                |     {player1_colour}     |                                |     {player2_colour}     |     
                |           |                                |           |
                |        {player1_number_card} |                                |        {player2_number_card} |         
                |___________|                                |___________|
        
        """)

        print("Player 1 won this round")
    elif player2_colour == "Y" and player1_colour == "R":
        player2_counter += 1

        print(f"""Player 1 got:                                Player 2 got:
                 ___________                                  ___________
                |           |                                |           |
                | {player1_number_card}        |                                | {player2_number_card}        |
                |           |                                |           |
                |     {player1_colour}     |                                |     {player2_colour}     |     
                |           |                                |           |
                |        {player1_number_card} |                                |        {player2_number_card} |         
                |___________|                                |___________|
        
        """)

        print("Player 2 won this round")
    elif player1_colour == "B" and player2_colour == "Y":
        player1_counter += 1

        print(f"""Player 1 got:                                Player 2 got:
                 ___________                                  ___________
                |           |                                |           |
                | {player1_number_card}        |                                | {player2_number_card}        |
                |           |                                |           |
                |     {player1_colour}     |                                |     {player2_colour}     |     
                |           |                                |           |
                |        {player1_number_card} |                                |        {player2_number_card} |         
                |___________|                                |___________|
        
        """)

        print("Player 1 won this round")
    elif player2_colour == "B" and player1_colour == "Y":
        player2_counter += 1

        print(f"""Player 1 got:                                Player 2 got:
                 ___________                                  ___________
                |           |                                |           |
                | {player1_number_card}        |                                | {player2_number_card}        |
                |           |                                |           |
                |     {player1_colour}     |                                |     {player2_colour}     |     
                |           |                                |           |
                |        {player1_number_card} |                                |        {player2_number_card} |         
                |___________|                                |___________|
        
        """)

        print("Player 2 won this round")
    elif player2_colour == player1_colour:

        print(f"""Player 1 got:                                Player 2 got:
                 ___________                                  ___________
                |           |                                |           |
                | {player1_number_card}        |                                | {player2_number_card}        |
                |           |                                |           |
                |     {player1_colour}     |                                |     {player2_colour}     |     
                |           |                                |           |
                |        {player1_number_card} |                                |        {player2_number_card} |         
                |___________|                                |___________|
        
        """)
        #Checks what happens when card colour is the same
        if player2_number > player1_number:
            player2_counter+=1
            print("Player 2 won this round because of a higher number on the card!")
        elif player1_number > player2_number:
            player1_counter+=1
            print("Player 1 won this round because of a higher number on the card!")

    
    print("")
    input("Write any character to continue: ")
    print("")

    cards -= 2


#Checks the counters
if player1_counter > player2_counter:
    print("Good job Player 1, you have won the game!")
elif player1_counter == player2_counter:
    print("It's a draw!")
else:
    print("Good job Player 2, you have won the game!")