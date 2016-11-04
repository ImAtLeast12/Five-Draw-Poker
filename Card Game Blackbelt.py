""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")


def showDeck():
    for i in range(NUMCARDS):
        print(cardLoc[i])
        
def clearDeck():
    print("Location of all cards")
    print("#" + "\t" + "card" + "\t" + "\t " + "Location")

    for y in range (len(suitName)):
        for x in range (len(rankName)): 
            cardIndex = x + (y*13)
            count = (str(rankName[x]) + " of " + str(suitName[y]))
            count = count.__len__()
            if (count < 8):
                countTabs = 3
            elif(count < 16):
                countTabs = 2
            elif(count < 24):
                countTabs = 1
                
            tabs = countTabs * "\t"
                
            cardLoc[cardIndex] = (str(cardIndex)) + "\t" +  rankName[x] + " of " + suitName[y] + tabs + "deck"
            
def assignCard(playerIndex):
    keepGoing = True
    while keepGoing:
        i = random()
        i *= NUMCARDS 
        i = int (i)
        if (cardLoc[i][(-1 * (playerName[0].__len__())):] == playerName[0]):
            cardLoc[i] = cardLoc[i][:(-1* (playerName[0].__len__()))]
            cardLoc[i] += playerName[playerIndex] 
            keepGoing = False
 
def showHand(playerIndex):
    for i in range(NUMCARDS): 
        if (cardLoc[i][(-1 * (playerName[playerIndex].__len__())):] == playerName[playerIndex]):
            print(cardLoc[i])
            
def main(): #What I want is to make a card game
            #however what cardgame should I make
            #Poker (hard), 21 mabey, go fish, 
    
    clearDeck()    
    for i in range(5): #each player gets five randomly assigned cards
        assignCard(PLAYER)
        assignCard(COMP)
    #The Player can change their hand
        #get rid of cards ("0,1,2,3,4") or just ("keep")
        #assign a new card for the ones they took out
    #Then the computer can change their cards
        #the computer will need to find a value of what cards are good
        #something similar to what the player did
    #Then scoring the cards
        #see who beat who

def score(playerIndex): #This needs the input of whos hand you are on
    #Sort the cards from greatest value to least A,K,Q,J,10, ... 3,2
    #to do this we will have to look at it's rankName
    hand = [0] * 5
    
    j = 0 #this is just the index for hand
    for i in range(NUMCARDS):
        if (cardLoc[i][(-1 * (playerName[1].__len__())):] == playerName[1]):
            hand[j] = i #this will assign the indexes of the cardlocation into hand
            j = +1 

    #Hand = [6,16,31,49,50]
            #stands for 7H, 4D, 6C, JC, QC

    #Now I should Sort them
            #should be 4D, 6C, 7H, JC, QC
                #or Just 4,6,7,J,Q

    #the High Hand is = Q or hand[4]






    #FOR TESTING PURPOSES I CAN SET HAND = [0,1,2,3,4] IF I WANT TO TEST THE FUNCTIONALITY
            


    
    
    #HIGH HAND above
            #I want to sort my cards from highest to lowest
    def Score(hand):
        #hand = [2,16,31,49,50]
        #look at card Location and get rid of the "index, of suit\t\tplayer"
        Arr = [-1] * 5
        Ar2 = [-1] * 5
        

        for y in range (len(hand)): #this will be the index for the CardLoc[y]
            for x in range (len(rankName)): # this will be the index for rankName[x]
                if (cardLoc[hand[y]].find(rankName[x]) != -1):
                    if (x == 0): #if the card is Ace
                        x = 13   #Ace is the best so make it 13
                    Arr[y] = x + 1  #Add another 1 so that "Three" = 3

        for y in range (len(hand)):
            for x in range (len(suitName)):
                if (cardLoc[hand[y]].find(suitName[x]) != -1):
                    Ar2[y] = x #this will tell me what suit they are

        #I need to do the same thing but for Hearts, Diamonds, Spades, and Clubs
        





        

        #hand = [2,16,31,49,50]                             BEFORE
        #Arr = ["Three", "Four", "Six", "Jack", "Queen"]    
        #What I want is = [3,4,6,11,12]                     AFTER
        HighCard = Arr[4]
        
                
                    

        scoring = [-1] * 10 #everything = -1 in scoring 2d array
        #scoring = [scoring] * (len(playerName) - 1) #this will make a 2d list of length 9 for (High, 1 Pair, 2 Pair, 3 of a Kind, Straight, Flush, Full house, Four of a Kind, Straight Flush, Royal Flush)

        scoring[0] = HighCard #Scoring = [12, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        #I should have a tuple for all of the hand combinations for what ever player I am on scoring[0] = [Q,0,0,0,0,0,0,0,0,0]
        #So when I am done the winner will be the one that has the highest 1

        


    #1 PAIR
        #USE Arr[] because it is ordered from greatest to least
        Pair1 = 0
        for i in range (5):
            if (Arr[0 + i] == Arr[1 + i]):
                Pair1 = Arr[0 + i]
                
        scoring[1] = Pair1 #This will tell if there is a pair and what kind of pair it was
        
        
    #2 PAIR

        
    #3 OF A KIND

        Pair3 = 0
        for i in range(3):
            if (Arr[0 + i] == Arr[1 + i]):
                if (Arr[1 + i] == Arr[2 + i]):
                    if (Arr[2 + i] == Arr [3 + i]):                   
                        Pair3 = Arr[0 + i]
        scoring[3] = Pair3

        
    #STRAIGHT
        straight = 0
        if (Arr[0] + 1== Arr[1]):
            if (Arr[1] + 1== Arr[2]):
                if (Arr[2] + 1 == Arr[3]):
                    if (Arr[3] + 1 == Arr[4]):
                        #this only works if it is from 0,1,2,3,4
                        straight = Arr[4]
        

        #This works for the others that wouldn't
        if(Arr[0] == 2):
            if(Arr[1] == 11): 
                if(Arr[2] == 12): 
                    if(Arr[3] == 13): 
                        if(Arr[4] == 14): 
                            print("good 2 high")
                            straight = 2
                            
            if(Arr[1] == 3): 
                if(Arr[2] == 12):
                    if(Arr[3] == 13):
                        if(Arr[4] == 14): 
                            print("good 3 high")
                            straight = 3
                if(Arr[2] == 4):
                    if(Arr[3] == 13): 
                        if(Arr[4] == 14): 
                            print("good 4 high")
                            straight = 4
                    if(Arr[3] == 5):
                        if(Arr[4] == 14): 
                            print("good 5 high")
                            straight = 5
        scoring[4] = straight
                    
        
        #I need to make sure that these are what it is equal to 
        #[ 2,11,12,13,14]
        #[ 2, 3,12,13,14]
        #[ 2, 3, 4,13,14]
        #[ 2, 3, 4, 5,14]

        
    #FLUSH
        flush = 0
        if (Ar2[0] == Ar2[1])
            if (Ar2[1] == Ar2[2])
                if (Ar2[2] == Ar2[3])
                    if (Ar2[3] == Ar2[4])
                        flush = Ar2[0] + 1
        scoring[5] = flush
        
    #FULL HOUSE
    #FOUR OF A KIND

        Pair4 = 0
        for i in range(2):
            if (Arr[0 + i] == Arr[1 + i]):
                if (Arr[1 + i] == Arr[2 + i]):
                    if (Arr[2 + i] == Arr[3 + i]):
                        Pair4 = Arr[0 + i]
        scoring[2] = Pair4 #if there is 4 all of the same value then this is equal to one of the cards
    #STRAIGH FLUSH
    #ROYAL FLUSH
        if (flush != 0 or -1)
            if (straight != 0 or -1)
    return -1
