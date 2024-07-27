import random

user_score = 0
computer_score = 0

list = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please type Rock/Paper/Scissor or Quit to Exit: ").lower()
    
    random_number = random.randint(0, 2)
    computer_pick = list[random_number]
    print("Computer picked", computer_pick)
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won")
        user_score += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_score += 1
        
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won")
        user_score += 1
        
    elif user_input == computer_pick:
        print("You both picked the same option. Try again")
        
    elif user_input == "quit":
        break
    
    elif user_input not in list:
        continue
    
    else:
        print("You lost")
        computer_score += 1
        
print("Your score = ", user_score)
print("Computer score = ", computer_score)
print("Thanks for Playing")
        