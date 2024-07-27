import random

print("Welcome to Number gussing game.")
number = random.randint(0, 10)

chances = 0

print("Guess a number between 1 to 10:")

while chances <5:
    guess = int(input())
    
    if guess == number:
        print("Congratulation you won!")
        break
    elif guess < number:
        print("Guess a higher number")
    else :
        print("Guess a lower number")
    chances +=1

if not chances < 5:
    print("Sorry you lost! the number is", number)