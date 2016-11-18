from random import *
# NUMCARDS = 52
# DECK = 0
# PLAYER = 1
# COMP = 2

# cardLoc = [0] * NUMCARDS


# playerName = ("deck", "player", "computer")

# def main():
    
#     player = Player()
#     player.name = "Player"
#     player.playerNum = 1

#     computer = Player()
#     computer.name = "Computers"
#     computer.isComputer = True
#     computer.playerNum = 2

    



    

#     clearDeck()
#     print("Location of all cards")
#     print("#" + "\t" + "card" + "\t" + "\t " + "Location")
#     for i in range(5):
#         player.assignCard(PLAYER)
#         computer.assignCard(COMP)
#     #showDeck()
#     print("\n")
#     print("Players Cards")
#     player.showHand(PLAYER)
#     print("\n") 
#     print("Computer Cards")
#     computer.showHand(COMP)

# def clearDeck():
#     cardLoc = [0]*NUMCARDS
    
# def showDeck():
#     p = []
#     for i in range(NUMCARDS):
#         p.append(printCard(i))
        
#     for i in range(len(p)):
#         print(str(p[i]))

# def printCard(cardIndex):
#     x = cardIndex % len(rankName)
#     y = cardIndex // len(rankName)

#     return ('{} \t {:5} of {} \t {}').format(cardIndex,rankName[x],suitName[y],cardLoc[cardIndex])

# class Player():
#     def __init__(self, name = "defalt",isComputer = False,hand = [],playerNum = 1):
#         self.name = name
#         self.isComputer = isComputer
#         self.hand = []
#         self.playerNum = playerNum

#     def assignCard(self,playerOn): #generate a random number from 0 to 51 that it is inside the deck
#         legalCards = []
#         for i in range(52):
#             if (cardLoc[i] == DECK): #tells me the cards that are left in the deck
#                 legalCards.append(i) #Stores that into legalCards
#         randNum = int(random()*len(legalCards)) #chooses an index in legalCards
#         cardLoc[legalCards[randNum]] = self.playerNum #The number rand chose cardLocation is now equal to your player number
#         self.hand.append(legalCards[randNum])
        

#     def showHand(self,playerOn):
#         print(self.hand)
#         for i in range(len(self.hand)):
#             print(self.hand[i])

class Deck():
    def __init__(self, num_cards):
        self.suit_name = ("hearts", "diamonds", "spades", "clubs")
        self.rank_name = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
        self.deck [num_cards];
        self.build_deck (num_cards)

    def build_deck (num_cards):
        if num_cards == 52:
            for i in range (0, 51):
                """ card constructor takes (card num from 0 to 12, suit name from 0 to 3, 
                    the string suit name, the string rank name) """
                self.deck[i] = Card( i % 13 , i / 13 , self.suit_name[i / 13] , self.rank_name[i % 13] )


class Card():
    def __init__(self, card_num, suit_num, suit_name, rank_name):
        self.card_num = card_num
        self.suit_num = suit_num;
        self.suit_name = suit_name;
        self.rank_name = rank_name;
        print ("constructed card ", print_card)
    
    def get_suit_num ():
        return self.card_suit

    def get_rank_num ():
        return self.card_num

    def print_card (self):
        return str("{} of {}").format(self.rank_name[self.card_num], self.suit_name[self.suit_num])
        

        

if (__name__ == "__main__"):
    main()
        
