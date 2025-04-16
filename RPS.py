import random

print()
print("_" * 50)
print("\nWelcome to Rock Paper Scissors with Python! \n")
print("_" * 50)
print("\nYou will have three options: \n\n 1. Rock \n 2. Paper \n 3. Scissors")
print("\nThe computer will at random choose one and the winner will be shown below!")

def rps_game():
    users_choice = int(input("Choose your number now: "))
    print()
    
    #if/elif/else statements for users input
    
    if users_choice == 1:
        print("You chose rock!")
        print("""    
           _________
        ---,     ____)_
                 _____)_
                 ______)
                _______)
       --,___________) 
              """)
    elif users_choice == 2:
         print("You chose paper!")
         print("""    
           _________
        ---,     ____)____
                     _____)_
                 ___________)
                ___________)
       --,______________) 
              """)
    elif users_choice == 3:
        print("You chose scissors!")
        print("""    
           _________
        ---,     ____)____
                     _____)_
                 ___________)
                ______)
       --,____________) 
              """)
    else:
        print("Sorry, invalid input. Please restart the program.")
        exit()
    
    
    
    #creating visual rock paper and scissors using print statements
    
    def rock():
        print("The computer chose rock!")
        print("""    
           _________
        ---,     ____)_
                 _____)_
                 ______)
                _______)
       --,___________) 
              """)
        
    def paper():
        print("The computer chose paper!")
        print("""    
           _________
        ---,     ____)____
                     _____)_
                 ___________)
                ___________)
       --,______________) 
              """)
        
    def scissor():
        print("The computer chose scissors!")
        print("""    
           _________
        ---,     ____)____
                     _____)_
                 ___________)
                ______)
       --,____________) 
              """)
    
    computer_rps = [rock, paper, scissor]
    
    computer_output = random.choice(computer_rps)
    
    
    computer_output()
    
    if users_choice == 1 and computer_output == rock:
        print("Its a draw! Play again! ")
    if users_choice == 1 and computer_output == paper:
        print("Computer won! ")
    if users_choice == 1 and computer_output == scissor:
        print("You won!")
    if users_choice == 2 and computer_output == rock:
        print("You won!")
    if users_choice == 2 and computer_output == paper:
        print("Its a draw! Play again! ")
    if users_choice == 2 and computer_output == scissor:
        print("Computer won!")
    if users_choice == 3 and computer_output == rock:
        print("Computer won!")
    if users_choice == 3 and computer_output == paper:
        print("You won!")
    if users_choice == 3 and computer_output == scissor:
        print("Its a draw! Play again! ")



while True:
    rps_game()
    user_input = str(input("Do you wish to play again? Type y for yes and n for no ").lower())
    if user_input == "n":
        break
