# Ask the user to enter scores between 0 and 100, inclusive
inNum = int (input ("Enter a score (negative to exit) "))
MIN_SCORES_REQUIRED = 3         # Need at least 3 scores
theScores = []      # Empty array
score_pass = 0 # 60 and 69  inclusive 
score_merit = 0 #  between 70 and 79  inclusive
score_distinction = 0 #  higher than 80
score_fail = 0

if (inNum > 100):
    print ("Maximum score is 100")

else:
    # A negative number terminates the loop

    while (inNum >= 0):
        theScores.append (inNum)    # Add each score to an array
        inNum = int (input ("Enter a score (negative to exit) "))
        # check whether it is a fail, pass, merit or distinction
        if inNum>=60 and inNum<=69:
            score_pass+=1
        elif inNum>=70 and inNum<=79:
            score_merit+=1
        elif inNum>=80:
            score_merit+=1
        else:
            score_fail +=1
        

# Check if we have minimum number of scores
if(len (theScores) >= MIN_SCORES_REQUIRED):
    print("There are ",len(theScores)," scores")
    print("The scores: ", theScores)
    print(score_fail," got a fail ",score_pass," got a pass ",score_merit," got a merit ",score_distinction," got a distinction" )
else:
    print ("At least three scores needed")

print ("Goodbye")

