import random

number = random.randint(1, 3)
print("Welcome to Rock Paper and Scissors game !")
user = input("Choose > > Rock,Paper,Scissors: ").capitalize()

if number == 1:
    system = "Rock"
elif number == 2:
    system = "Paper"
else:
    system = "Scissors"

print(f"Your choice : {user}")
print(f"My choice : {system}")

if user != "Rock" and user != "Paper" and user != "Scissors":
    print("Invalid Input")
elif user == system:
    print("Draw")
else:
    if user == "Rock" and system == "Paper" or \
            user == "Paper" and system == "Scissor" or \
            user == "Scissor" and system == "Rock":
        print("You lose")
    else:
        print("You win")

