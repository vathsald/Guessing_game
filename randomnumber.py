import random


def Play_game():
    
    guess = -1
    attempt = 0
    print("Choose difficulty level  (1.Easy,2.Medium,3.Hard)")
    try:
        dlevel=int(input("Enter the level number: "))
    except:
        print("Invalid level")
        return
    if dlevel==1:
        chances=15
        limit=50
    elif dlevel==2:
        chances=10
        limit=75
    elif dlevel==3:
        chances=5
        limit=100
    else:
        print("Invalid level")
        return
    num = random.randint(1,limit)
    print(f"You get {chances} attempts")
    print("Good luck guessing:)")
    for i in range(chances):
        print("Attempts left:", chances-i)
        try:
            guess = int(input("Enter your guess: "))
        except:
            print("Invalid Guess")
            continue
        attempt+=1
        if guess > num:
            print("Too high! Try lower")

        elif guess < num:
            print("Too low! Try higher")

        else:
            print("Correct!")
            print("Number of attemps", attempt)
            score=chances-attempt+1
            print("Your Score was:",score)
            break
    else:
        print("Game over,Correct number was", num)


Play_game()
while True:
    decision = input("If u want to play again (y/n)")
    if decision.lower() == "y":
        Play_game()
    elif decision.lower()=="n":
        print("Thank you for Playing")
        break
    else:
        print("Invalid decision")
        continue