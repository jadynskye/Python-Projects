#This number guessing game was to help me work on local and global varibles 
#Future improvments - add a while loop to keep the game going until user is done
import random 

correct_number = random.randint(1,100)

players_choice = ''

def intro_to_game(guess):
    print("Welcome to the Number Guessing Game!")
    guess = input("I'm thinking of a number between 1 and 100\n" 
    "Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    return(guess)



def easy_game():
    global correct_number

    attempts = 10
    gameover = False

    while gameover == False:
        if attempts > 0 :
            number_guess = int(input(f"You have {attempts} attempts remaining to guess the number\n "
                    "Make a guess: "))
            if number_guess > correct_number:
                print("Sorry that number is too high! Please, try again.")
                attempts -= 1 
            elif number_guess < correct_number:
                print("Sorry that number is too low! Please, try again.")
                attempts -= 1 
            else:
                print("Horray! You got the right number!")
                gameover = True
        else:
            print("Sorry, you did not get the number! Please restart the game")
            gameover = True

def hard_game():
    global correct_number

    attempts = 5
    gameover = False

    while gameover == False:
        if attempts > 0 :
            number_guess = int(input(f"You have {attempts} attempts remaining to guess the number\n "
                    "Make a guess: "))
            if number_guess > correct_number:
                print("Sorry that number is too high! Please, try again.")
                attempts -= 1 
            elif number_guess < correct_number:
                print("Sorry that number is too low! Please, try again.")
                attempts -= 1 
            else:
                print("Horray! You got the right number!")
                gameover = True
        else:
            print("Sorry, you did not get the number! Please restart the game")
            gameover = True




guess = intro_to_game(players_choice)

if guess == "easy":
    easy_game()
elif guess == "hard":
    hard_game()
else:
    print("Sorry you did not choose easy or hard. Please try again")
    intro_to_game(players_choice)
