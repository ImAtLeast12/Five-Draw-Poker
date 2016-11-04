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
        
def showDeck():
    for i in range(NUMCARDS):
        print(cardLoc[i])
 
def showHand(playerIndex):
    hand = []
    for i in range(NUMCARDS): 
        if (cardLoc[i][(-1 * (playerName[playerIndex].__len__())):] == playerName[playerIndex]):
            print(cardLoc[i])
            
            if (cardLoc[i][1:2] == "\t"):
                hand.append(i) #= cardLoc[i][:1]#either is one digit 
            else:
                hand.append(i) #= cardLoc[i][:2]#or 2 digits
    return hand

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

def Score(playerIndex): #This needs the input of whos hand you are on

    Sort = []
    i = 1
    for i in range(len(playerName)):
        hand = showHand(i) #this stores the hand you are working on for which ever player you are on
        Sort.append(Sort(hand))
    
    Scoring = [HighCard(hand), OnePair(hand), TwoPair(hand),ThreeOfAKind(hand), Straight(hand),Flush(hand),FullHouse(hand),FourOfAKind(hand),StraightFlush(hand),RoyalFlush(hand)]
    return Scoring

    
def Sort(hand):
    #hand = [2,16,31,49,50]
    #look at card Location and get rid of the "index, of suit\t\tplayer"
    Arr = [-1] * 5
    Ar2 = [-1] * 5
    
    for y in range (len(hand)): #
        for x in range (len(rankName)): #
            if (cardLoc[hand[y]].find(rankName[x]) != -1): # If it finds a match        
                if (x == 0): #
                    x = 13   #
                Arr[y] = x + 1  #All of this works I think I just need to sort it from least to greatest
    Arr.sort()

    for y in range (len(hand)):
        for x in range (len(suitName)):
            if (cardLoc[hand[y]].find(suitName[x]) != -1):
                Ar2[y] = x #this will tell me what suit they are

    #I need to do the same thing but for Hearts, Diamonds, Spades, and Clubs
                
    return Arr, Ar2 #This gives me my precious Arr, Ar2 So that I can use them in the Scoring

def HighCard (Arr,Ar2):
    
    #hand = [2,16,31,49,50]                             BEFORE
    #Arr = ["Three", "Four", "Six", "Jack", "Queen"]    
    #What I want is = [3,4,6,11,12]                     AFTER
    HighCard = Arr[4]
    return HighCard
            
                

    #scoring = [-1] * 10 #everything = -1 in scoring 2d array
    #scoring = [scoring] * (len(playerName) - 1) #this will make a 2d list of length 9 for (High, 1 Pair, 2 Pair, 3 of a Kind, Straight, Flush, Full house, Four of a Kind, Straight Flush, Royal Flush)

    #scoring[0] = HighCard #Scoring = [12, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    #I should have a tuple for all of the hand combinations for what ever player I am on scoring[0] = [Q,0,0,0,0,0,0,0,0,0]
    #So when I am done the winner will be the one that has the highest 1

    


#1 PAIR
def OnePair (hand,Arr,Ar2):
    #USE Arr[] because it is ordered from greatest to least
    OnePair = 0
    for i in range (4):
        if (Arr[0 + i] == Arr[1 + i]):
            OnePair = Arr[0 + i]
            
    return OnePair #This will tell if there is a pair and what kind of pair it was
    
    
#2 PAIR
def TwoPair (hand,Arr,Ar2):
    TwoPair = 0
    if Arr[0] == Arr[1]:
        if Arr[2] == Arr[3]:
            TwoPair = Arr[3]
        if Arr[3] == Arr[4]:
            TwoPair = Arr[4]
    if Arr[1] == Arr[2]:
        if Arr[3] == Arr[4]:
            TwoPair = Arr[4]
    return TwoPair

    
#3 OF A KIND
def ThreeOfAKind (hand,Arr,Ar2):
    ThreeOfAKind = 0
    for i in range(3):
        if (Arr[0 + i] == Arr[1 + i]):
            if (Arr[1 + i] == Arr[2 + i]):
                if (Arr[2 + i] == Arr [3 + i]):                   
                    ThreeOfAKind = Arr[0 + i]
    return ThreeOfAKind

#STRAIGHT
def Straight (hand,Arr,Ar2):
    Straight = 0
    if (Arr[0] + 1== Arr[1]):
        if (Arr[1] + 1== Arr[2]):
            if (Arr[2] + 1 == Arr[3]):
                if (Arr[3] + 1 == Arr[4]):
                    #                             [         ]         [         ]
                    #this only works if it is from 0,1,2,3,4,5,6,7,8,9,10,J,Q,K,A
                    Straight = Arr[4]
    

    #This works for the others that wouldn't
    if(Arr[0] == 2):
        if(Arr[1] == 11): 
            if(Arr[2] == 12): 
                if(Arr[3] == 13): 
                    if(Arr[4] == 14): 
                        print("good 2 high")
                        Straight = 2
                        
        if(Arr[1] == 3): 
            if(Arr[2] == 12):
                if(Arr[3] == 13):
                    if(Arr[4] == 14): 
                        print("good 3 high")
                        Straight = 3
            if(Arr[2] == 4):
                if(Arr[3] == 13): 
                    if(Arr[4] == 14): 
                        print("good 4 high")
                        Straight = 4
                if(Arr[3] == 5):
                    if(Arr[4] == 14): 
                        print("good 5 high")
                        Straight = 5
    return Straight
                
    
    #I need to make sure that these are what it is equal to 
    #[ 2,11,12,13,14]
    #[ 2, 3,12,13,14]
    #[ 2, 3, 4,13,14]
    #[ 2, 3, 4, 5,14]

    
#FLUSH
def Flush (hand,Arr,Ar2):
    flush = False
    if (Ar2[0] == Ar2[1]):
        if (Ar2[1] == Ar2[2]):
            if (Ar2[2] == Ar2[3]):
                if (Ar2[3] == Ar2[4]):
                    flush = True
    return flush
    
#FULL HOUSE
def FullHouse(hand,Arr,Ar2):
    FullHouse = 0
    if Arr[0] == Arr[1]:
        if Arr[1] == Arr[2]:
            if Arr[3] == Arr[4]:
                FullHouse = Arr[0]
        if Arr[2] == Arr[3]:
            if Arr[3] == Arr[4]:
                FullHouse = Arr[4]
    return FullHouse
    
#FOUR OF A KIND
def FourOfAKind (hand):
    FourOfAKind = 0
    for i in range(2):
        if (Arr[0 + i] == Arr[1 + i]):
            if (Arr[1 + i] == Arr[2 + i]):
                if (Arr[2 + i] == Arr[3 + i]):
                    FourOfAKind = Arr[0 + i]
    return FourOfAKind

#STRAIGH FLUSH
def StraightFlush (hand):
    StraightFlush = False
    if Straight(hand):
        if Flush(hand):
            StraightFlush = True
    return StraightFlush
    
    #return (Straight(hand) and Flush(hand))
    
#ROYAL FLUSH
def RoyalFlush (hand):
    RoyalFlush = False
    if (StraightFlush(hand)):
            if (HighCard(hand) == 14):
                RoyalFlush = True
    return RoyalFlush
    #return (StraightFlush(hand) and HighCard == 14)        #this will return true if hand was Straight, Flush, and HighCard
                                                            #Else it will return False




