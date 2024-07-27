print('Welcome to my Quiz game')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Let's begain the game")

score = 0

answer = input("What does HTML stand for? ")
if answer.lower() == "hyper text markup language":
    print("Correct")
    score +1
else:
    print("Incorrect")
    
answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print("Correct")
    score +1
else:
    print("Incorrect")
    
answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheet":
    print("Correct")
    score +1

else:
    print("Incorrect")
    
answer = input("What does DBMS stand for? ")
if answer.lower() == "data base management system":
    print("Correct")
    score +1
else:
    print("Incorrect")
    
print("you got " + str(score) + " questions correct")
print("you scored " + str((score / 4)*100) + " marks")