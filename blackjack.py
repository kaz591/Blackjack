#Creacion de un juego de blackjack con POO
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace' :11}

playing = True

class Card():
    """Creacion de el formato de cartas
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    """Crea el deck con las 52 cartas
    """
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank, suit))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        card = self.deck.pop()
        return card
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return f"The deck has {deck_comp}"

class Hand():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.aces = 0
    def add_card(self, card):
        self.hand.append(card)
        self.hand_value +=  values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_ace(self):
        while self.hand_value > 21 and self.aces:
            self.value -= -10
            self.aces -= 1

class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f"You have {player_chips.total} chips, how many chips you want to bet: "))
        except ValueError:
            print("Sorry you need to input a valid number")
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have that many chips.")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_ace

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    print(f"\nDealer's Hand: \n<card hidden> \n{dealer.hand[1]}")
    print("\nPlayer's Hand:",*player.hand, sep="\n")

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.hand, sep='\n ')
    print("Dealer's Hand =",dealer.hand_value)
    print("\nPlayer's Hand:", *player.hand, sep='\n ')
    print("Player's Hand =",player.hand_value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    print('Welcome to BlackJack at Casinoganas! Get as close to 21 as you can without going over!\n\
    Dealer hits until it reaches 17. Aces count as 1 or 11.')

    deck = Deck()
    deck.shuffle()
    player_chips = Chips()

    player1 = Hand()
    player1.add_card(deck.deal())
    player1.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    take_bet(player_chips)                      #prompts the player for the bet amount
    show_some(player1,dealer)          # Show cards (but keep one dealer card hidden)

    while playing:

        hit_or_stand(deck,player1)          # Prompt for Player to Hit or Stand

        show_some(player1,dealer)      # Show cards (but keep one dealer card hidden)

        if player1.hand_value > 21:         # If player's hand exceeds 21, run player_busts() and break out of loop
            player_busts(player1,dealer,player_chips)
            break
    if player1.hand_value <= 21:            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        while dealer.hand_value < 17:
            hit(deck,dealer)

        show_all(player1,dealer)       # Show all cards

        if dealer.hand_value > 21:         # Run different winning scenarios
            dealer_busts(player1,dealer,player_chips)

        elif dealer.hand_value > player1.hand_value:
            dealer_wins(player1,dealer,player_chips)

        elif dealer.hand_value < player1.hand_value:
            player_wins(player1,dealer,player_chips)

        else:
            push(player1,dealer)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at",player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break