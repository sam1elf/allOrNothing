
""" to do: make subsequent rolls only use "diceRemaining"
    cut either diceRoll or diceDescription before zip()  """


import os
import random

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#print a headline
print "All or Nothing!"

score = 0
diceRemaining = 6

#define functions
def doARoll():
    global diceRemaining
    global score

    #set 6 random numbers from 1-6 to the list: diceRoll
    diceRoll = [random.randint(1,6), random.randint(1,6), random.randint(1,6), 
                 random.randint(1,6), random.randint(1,6), random.randint(1,6)]

    #create a list for sorting the dice
    diceDescription = ['1. dice: ', '2. dice: ', '3. dice: ', '4. dice: ', '5. dice: ', '6. dice: ']

    #combine the lists
    currentRoll = zip(diceDescription, diceRoll)

    #print both lists together
    for key in currentRoll:
        print key

    #store result in variables
    ones = diceRoll.count(1)
    twos = diceRoll.count(2)
    threes = diceRoll.count(3)
    fours = diceRoll.count(4)
    fives = diceRoll.count(5)
    sixes = diceRoll.count(6)

    #initialize variables
    special = 0
    pairs = 0 
    

    #value the roll

    #straight
    if ones == 1 and twos == 1 and threes == 1 and fours == 1 and fives == 1 and sixes == 1:
        score += 1250
        special = 1
        diceRemaining = 6

    #3pair
    if ones == 2:
        pairs += 1
    if twos == 2:
        pairs += 1
    if threes == 2:
        pairs += 1
    if fours == 2:
        pairs += 1
    if fives == 2:
        pairs += 1
    if sixes == 2:
        pairs += 1
    #check if number of pairs is exactly 3
    if pairs == 3:
        score += 500
        special = 2
        diceRemaining = 6

    #no special
    if special == 0:
        if ones == 1:
            score += 100
            diceRemaining -= 1
        elif ones == 2:
            score += 200
            diceRemaining -= 2
        elif ones == 3:
            score += 1000
            diceRemaining -= 3
        elif ones == 4:
            score += 2000
            diceRemaining -= 4
        elif ones == 5:
            score += 4000
            diceRemaining -= 5
        elif ones == 6:
            score += 8000
            diceRemaining = 6

        if twos == 3:
            score += 200
            diceRemaining -= 3
        elif twos == 4:
            score += 400
            diceRemaining -= 4
        elif twos == 5:
            score += 800
            diceRemaining -= 5
        elif twos == 6:
            score += 1600
            diceRemaining = 6

        if threes == 3:
            score += 300
            diceRemaining -= 3
        elif threes == 4:
            score += 600
            diceRemaining -= 4
        elif threes == 5:
            score += 1200
            diceRemaining -= 5
        elif threes == 6:
            score += 2400
            diceRemaining = 6

        if fours == 3:
            score += 400
            diceRemaining -= 3
        elif fours == 4:
            score += 800
            diceRemaining -= 4
        elif fours == 5:
            score += 1600
            diceRemaining -= 5
        elif fours == 6:
            score += 3200
            diceRemaining = 6

        if fives == 1:
            score += 50
            diceRemaining -= 1
        elif fives == 2:
            score += 100
            diceRemaining -= 2
        elif fives == 3:
            score += 500
            diceRemaining -= 3
        elif fives == 4:
            score += 1000
            diceRemaining -= 4
        elif fives == 5:
            score += 2000
            diceRemaining -= 5
        elif fives == 6:
            score += 4000
            diceRemaining = 6

        if sixes == 3:
            score += 600
            diceRemaining -= 3
        elif sixes == 4:
            score += 1200
            diceRemaining -= 4
        elif sixes == 5:
            score += 2400
            diceRemaining -= 5
        elif sixes == 6:
            score += 4800
            diceRemaining = 6

    #if none of the above applies
    if score == 0:
        diceRemaining = 0

    #call rollAgain function
    rollAgain()


def rollAgain():
    print "Dice remaining: " + str(diceRemaining)
    print "Score: " + str(score)
    #determine if there are dice left
    if diceRemaining >= 1:
        print "Would you like to roll again?"
        answer = raw_input()
        
        if answer != 'y' and answer != 'n' and answer != "yes" and answer != "no":
            print "type y/yes or n/no please."
            rollAgain() #answer not clear, ask again
        elif answer == 'y' or answer == 'yes':
            doARoll() #roll again
        elif answer == 'n' or answer == 'no':
            raise SystemExit #stop program
    else:
        print "No more options"
        raise SystemExit

#execute program
doARoll()

