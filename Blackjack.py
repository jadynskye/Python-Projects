'''
Jadyn Reid  
Date: August 6, 2025  

Description: This project is a simple text-based Blackjack game made using Python, where you play against the dealer.  
It deals two cards to both players, checks for Blackjack, handles Aces (11 or 1), and lets the user choose to hit or pass.  
The dealer draws until they reach at least 17. The program calculates scores, compares them, and announces the winner.  
To build it, I used functions, lists, conditionals, loops, user input, and the random module to simulate drawing cards.  
This game was honestly pretty hard to finish — I even had to sketch out a flowchart to figure out the logic. But overall,  
it was fun to make, and I’m proud I didn’t give up.

'''

import random 

def intro():
 
    print("\nWelcome to Jadyns coded version of ")

    print( '''
            _     _            _    _            _    
            | |   | |          | |  (_)          | |   
            | |__ | | __ _  ___| | ___  __ _  ___| | __
            | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
            | |_) | | (_| | (__|   <| | (_| | (__|   < 
            |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\-|
                                    _/ |                
                                |__/                 
        ''')


intro()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

users_cards = []
computers_cards = []

# Function to randomly choose card from list cards
def deal_card():
    """ Returns a random card from list 'cards' """
    random_card = random.choice(cards)
    return random_card


# Function to calculate each score
def calculate_score(hand):
    '''Function to calculate the score of a hand, returns 0 for blackjack'''

    if sum(hand) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(hand) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(hand)

# Deal initial cards 
for _ in range(2):
    users_cards.append(deal_card())
    computers_cards.append(deal_card())

print("The cards that were drawn were: ")
print(f"Your cards are {users_cards}")
print(f"The dealers first card is {computers_cards[0]}")

# Main logic game
gameover = False

while not gameover:
    user_score = calculate_score(users_cards)
    dealer_score = calculate_score(computers_cards)

    print(f"\nYour current hand: {users_cards}, current score: {user_score}")
    
    if user_score == 0:
        print("Blackjack! You win!")
        gameover = True
    elif user_score > 21:
        print("You went over. You lose.")
        gameover = True
    else:
        another_card = input("Type 'y' to get another card, 'n' to pass: ").lower()
        if another_card == 'y':
            users_cards.append(deal_card())
        else:
            gameover = True

# Dealer's turn
while calculate_score(computers_cards) < 17 and gameover is False:
    computers_cards.append(deal_card())

user_score = calculate_score(users_cards)
dealer_score = calculate_score(computers_cards)

print(f"\nYour final hand: {users_cards}, final score: {user_score}")
print(f"Dealer's final hand: {computers_cards}, final score: {dealer_score}")

# Determine the winner
def compare(user, dealer):
    if user > 21:
        return "You went over. You lose!"
    if dealer > 21:
        return "Dealer went over. You win!"
    if user == dealer:
        return "Draw!"
    if user == 0:
        return "Blackjack! You win!"
    if dealer == 0:
        return "Dealer has Blackjack! You lose."
    if user > dealer:
        return "You win!"
    else:
        return "You lose"

print(compare(user_score, dealer_score))
