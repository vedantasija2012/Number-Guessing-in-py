import random
RandNo=random.randint(1, 100)

user_guess=None
guesses=0

while user_guess!=RandNo:
    user_guess=int(input("Enter your Guess: "))
    guesses+=1
    if user_guess==RandNo:
        print("You Guessed the Number Right :)")
    elif user_guess<RandNo:
        print("Higher Number please!")
    else:
        print("Lower Number please!")
print(f"You Guessed the Number in {guesses} Guesses")

with open('NumberGuessing_in_py\highScore.txt', 'r') as f:
    highscore=int(f.read())

if guesses<highscore:
    print("Congratulations! You made a new High Score :)")
    with open('NumberGuessing_in_py\highScore.txt', 'w') as f:
        f.write(str(guesses))