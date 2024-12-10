class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit}({self.value})"
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def __str__(self):
        return f"{self.cards}"


    def shuffle(self):
        import random
        random.shuffle(self.cards)  

    def deal(self):
        player_hand = [self.cards.pop(0), self.cards.pop(12)]
        dealer_hand = [self.cards.pop(24), self.cards.pop(36)]

        return player_hand, dealer_hand
    
    def player_hit(self):
        return self.cards.pop()
    

def dealerTurn(deck,dealer_value, dealer_hand):
    if dealer_value < 17 and isAce(dealer_hand) == 0:
        while dealer_value < 17:
            print("Dealer must hit!")
            new_card = deck.cards.pop()
            print("Dealer pulled a " + new_card.value + "!")
            input("Press enter to continue...")
            new_value = cardValue(new_card.value)
            dealer_value += new_value
            print("Dealer now has " + str(dealer_value) + "!")
            input("Press enter to continue...")
        return dealer_value
    elif dealer_value <= 17 and isAce(dealer_hand) == 1:
        while dealer_value <= 17:
            print("Dealer must hit!")
            new_card = deck.cards.pop()
            print("Dealer pulled a " + new_card.value + "!")
            input("Press enter to continue...")
            new_value = cardValue(new_card.value)
            dealer_value += new_value
            print("Dealer now has " + str(dealer_value) + "!")
            input("Press enter to continue...")
        return dealer_value
    elif dealer_value < 17 and isAce(dealer_hand) == 2:
        while dealer_value < 17:
            print("Dealer must hit!")
            new_card = deck.cards.pop()
            print("Dealer pulled a " + new_card.value + "!")
            input("Press enter to continue...")
            new_value = cardValue(new_card.value)
            dealer_value += new_value
            print("Dealer now has " + str(dealer_value) + "!")
            input("Press enter to continue...")
        return dealer_value
    else:
        return dealer_value
    
def finalizeHand(dealer_value, player_value):
    if dealer_value > 21:
        print("YOU WIN! Dealer busted!")
        input("Press enter to continue...")
    elif dealer_value > player_value:
        print("You Lose...")
        input("Press enter to continue...")
    elif dealer_value == player_value:
        print("You pushed.")
    else:
        print("YOU WIN!")
        input("Press enter to continue...")
    
def isAce(hand):
    count = 0
    for i in hand:
        if i.value == "Ace":
            count += 1
    return count  

def cardValue(card_value):
    if card_value in ["Jack", "Queen", "King"]:
        return 10
    elif card_value == "Ace":
        return 1
    else:
        return int(card_value)
    
def WelcomePlayer():
    print("Welcome lets get into the rules!")
    input("Press enter to continue...")
    print("We will be playing with one deck shuffled after every hand. Dealer must hit on a soft 17. Other than that have fun!")
    input("Press enter to continue...")

def BlackjackHand():
    while True:
        deck = Deck()
        deck.shuffle()
        player_hand, dealer_hand = deck.deal()
        player_value = 0
        dealer_value = 0
        for i in range (2):
            player_value += cardValue(player_hand[i].value)
            dealer_value += cardValue(dealer_hand[i].value)
        if isAce(dealer_hand) >= 1:
            dealer_value += 10
        if isAce(player_hand) >= 1:
            player_value += 10
        print("The player has " + str(player_value) + " and the dealer is showing a " + dealer_hand[0].value + "!")
        input("Press enter to continue...")
        if player_value == 21 & dealer_value == 21:
            print("Its a push!")
            input("Press enter to continue...")
        elif player_value == 21:
            print("Blackjack! You win!")
            input("Press enter to continue...")
        elif dealer_value == 21:
            print("Dealer wins...")
            input("Press enter to continue...")
        else:
            while True:
                choice = input("Would you like to hit or stay? (h/s)")
                if choice == "h":
                    new_card = deck.player_hit()
                    player_value += cardValue(new_card.value)
                    input("You now have " + str(player_value) + "! Press enter to continue...")
                    if player_value >= 21:
                        break
                elif choice == "s":
                    break
                else:
                    choice = input("Would you like to hit or stay? (h/s)")
            if player_value > 21:
                print("You Lose... You busted!")
                input("Press enter to continue...")
            else:
                print("The player has " + str(player_value) + "! The dealer flipped a " + dealer_hand[1].value + " and has " + str(dealer_value) + "!")
                input("Press enter to continue...")
                dealer_value = dealerTurn(deck, dealer_value, dealer_hand)
                finalizeHand(dealer_value, player_value)
                cont = input("If you would like to exit please enter 'e'! Otherwise hit enter!")
                exit = True
                while exit:
                    if cont == "e":
                        print("Goodbye!")
                        exit = False
                    else:
                        break
                if not exit:
                    break
WelcomePlayer()
BlackjackHand()
