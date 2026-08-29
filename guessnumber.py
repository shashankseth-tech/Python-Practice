import random

computer = random.randint(1,10)

for i in range(3):
    a = int(input("Guess the number: "))
    if a == computer:
        print("You Won")
        break
    else:
        print("Wrong Answer")
else:
    print("You Lost")
    print("Computer Won",computer)
