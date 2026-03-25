

import random

def Play_game():
    num = random.randint(1, 100)
    guess=-1
    attempt=0
    for i in range(2):
        guess=int(input("Enter your guess : "))
        attempt+=1
        if guess > num:
            print("Too high")
    
        elif guess < num:
            print("Too low")
    
        else:
            print("Correct!")
            break
    else:
        print("Game over,Correct number was",num)
    print("number of attemps",attempt)  
Play_game()
x=0
while x==0:
    decision=input("If u want to play again (y/n)")
    if decision.lower == 'y' :
        Play_game()
    else:
        print("Thank you for Playing")
        x=1
