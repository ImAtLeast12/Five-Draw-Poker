""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
#so far this is looking pretty nice
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


def clearDeck(): #The assigns and initalizes all of the cards to deck 
    for i in range (NUMCARDS):
        cardLoc[i] = DECK

def assignCard(playerIndex): #This assigns a random card to whichever player
    keepGoing = True
    while keepGoing:
        i = int (random() * NUMCARDS)
        if (cardLoc[i] == DECK): 
            cardLoc[i] = playerIndex 
            keepGoing = False #I may need to check to see if all of the cards are deck first but that is a later mater

def showDeck(): #shows the location for all of the cards
    print("Location of all cards")
    print("#" + "\t" + "card" + "\t" + "\t " + "Location")
    for i in range(NUMCARDS):
        print(printCard(cardLoc,i))
    print("\n")

def showHand(playerIndex): #
    for i in range(NUMCARDS): 
        if (cardLoc[i] == playerIndex):
            print(printCard(cardLoc,i)) 
    print("\n")

def printCard(cardLoc, i): #prints the card you are looking for assuming you give the array ardlocation and it's 
    for y in range(len(suitName)):
        for x in range (len(rankName)):
            if (x+(y *13) == i):
                return ('{:3}  {:5} of {:10} {}'.format(str(i),str(rankName[x]),str(suitName[y]),str(playerName[cardLoc[i]])))
            
def main():
    clearDeck() #This assigns all of the cards to deck
    for i in range(5): #This deals out 5 cards to the players
        assignCard(PLAYER) 
        assignCard(COMP)
    showDeck() #This prints the deck
    showHand(PLAYER) #This prints the players hand
    showHand(COMP)  #This prints the computers hand








    
def Sort(hand): #this sorts the hand and outputs a tuple Arr,Ar2 #Arr is a list of the hand sorted by their rank, #Ar2 is a list of the hand sored by suit
#Sort allows me to use Arr, and Ar2 in the scoring functions
    Arr = [-1] * 5
    Ar2 = [-1] * 5
    
    for y in range (len(hand)): 
        for x in range (len(rankName)): 
            if (cardLoc[hand[y]].find(rankName[x]) != -1): 
                if (x == 0): 
                    x = 13   
                Arr[y] = x + 1  
    Arr.sort()

    for y in range (len(hand)):
        for x in range (len(suitName)):
            if (cardLoc[hand[y]].find(suitName[x]) != -1):
                Ar2[y] = x 

               
    return Arr, Ar2





def HighCard (Arr): #Given Arr, Highcard finds the highest card
    
    HighCard = Arr[4]
    return HighCard
            
#1 PAIR
def OnePair (Arr): #Given Arr OnePair finds if they have any pairs #only keeps the highest one
    OnePair = 0
    for i in range (4):
        if (Arr[0 + i] == Arr[1 + i]):
            OnePair = Arr[0 + i]
            
    return OnePair 
    
#2 PAIR
def TwoPair (Arr): #Given Arr TwoPair finds if they have two pairs #(Ex (5,5,7,A,A))
    TwoPair = 0
    if Arr[0] == Arr[1]:
        if Arr[2] == Arr[3]:
            TwoPair = Arr[3]  #Ex(5,5,6,6,6) or (5,5,6,6,J)
        if Arr[3] == Arr[4]:
            TwoPair = Arr[4]  #Ex(5,5,5,K,K) or (5,5,7,K,K)
    if Arr[1] == Arr[2]:
        if Arr[3] == Arr[4]:  
            TwoPair = Arr[4]  #Ex(J,J,J,A,A) or (5,J,J,A,A)
    return TwoPair

    
#3 OF A KIND
def ThreeOfAKind (Arr): #Given Arr ThreeOfAKind finds if they have 3 of the same in a list
    #Since Arr is sorted by Least to Greatest I only have so cycle a few times
    ThreeOfAKind = 0
    for i in range(3):
        if (Arr[0 + i] == Arr[1 + i]):
            if (Arr[1 + i] == Arr[2 + i]):
                if (Arr[2 + i] == Arr [3 + i]):                   
                    ThreeOfAKind = Arr[0 + i] #Ex(3,3,3,10,10) or (A,3,3,3,3)
    return ThreeOfAKind

#STRAIGHT
def Straight (Arr):
    Straight = 0

    if(Arr[0] + 1 == Arr[1]):
        if(Arr[1] + 1 == Arr[2]):
            if(Arr[2] +1 == Arr[3]):
                if(Arr[3] + 1 == Arr[4])
                Straight = Arr[4]
                    Straight = HighCard(Arr)

    
    if (Arr[0] + 1== Arr[1]):
        if (Arr[1] + 1== Arr[2]):
            if (Arr[2] + 1 == Arr[3]):
                if (Arr[3] + 1 == Arr[4]): #Ex(10,J,Q,K,A) or (2,3,4,5,6)
                    #                             [         ]         [         ]
                    #this only works if it is from  0,1,2,3,4,5,6,7,8,9,10,J,Q,K,A
                    Straight = Arr[4]
                    
    

    #This works for the others that wouldn't
    if(Arr[0] == 2):
        if(Arr[1] == 11): 
            if(Arr[2] == 12): 
                if(Arr[3] == 13): 
                    if(Arr[4] == 14): 
                        print("good 2 high") 
                        Straight = 2 #Ex(2,J,Q,K,A)
                        
        if(Arr[1] == 3): 
            if(Arr[2] == 12):
                if(Arr[3] == 13):
                    if(Arr[4] == 14): 
                        print("good 3 high")
                        Straight = 3 #Ex(2,3,Q,K,A)
            if(Arr[2] == 4):
                if(Arr[3] == 13): 
                    if(Arr[4] == 14): 
                        print("good 4 high")
                        Straight = 4 #Ex(2,3,4,K,A)
                if(Arr[3] == 5):
                    if(Arr[4] == 14): 
                        print("good 5 high")
                        Straight = 5 #Ex(2,3,4,5,A)


    
    return Straight
                
    
    #I need to make sure that these are what it is equal to 
    #[ 2,11,12,13,14]
    #[ 2, 3,12,13,14]
    #[ 2, 3, 4,13,14]
    #[ 2, 3, 4, 5,14]

    
#FLUSH
def Flush (Ar2): #Given Ar2 Flush finds if all of the ones are the same suit 
    flush = False 
    if (Ar2[0] == Ar2[1]):
        if (Ar2[1] == Ar2[2]):
            if (Ar2[2] == Ar2[3]):
                if (Ar2[3] == Ar2[4]):
                    flush = True #Ex(0,0,0,0,0)
    return flush
    
#FULL HOUSE
def FullHouse(Arr):
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
def FourOfAKind (Arr):
    FourOfAKind = 0
    for i in range(2):
        if (Arr[0 + i] == Arr[1 + i]):
            if (Arr[1 + i] == Arr[2 + i]):
                if (Arr[2 + i] == Arr[3 + i]):
                    FourOfAKind = Arr[0 + i]
    return FourOfAKind

#STRAIGH FLUSH
def StraightFlush (Arr,Ar2):
    StraightFlush = False
    if Straight(hand):
        if Flush(hand):
            StraightFlush = True
    return StraightFlush
    
    
#ROYAL FLUSH
def RoyalFlush (Arr,Ar2):
    RoyalFlush = False
    if (StraightFlush(hand)):
            if (HighCard(hand) == 14):
                RoyalFlush = True
    return RoyalFlush
