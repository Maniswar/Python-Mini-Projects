##############     PROJECT 1       #######

import random

rock     = 0
paper    = 1
scissors = 2

user     = int(input("Enter your choice type 0 for 'rock', type 1 for 'paper', type 2 for 'scissors': "))
computer = random.randrange(0,3)
if user >= 3 or user <0:
    print("Invalid input")
else:
    print(f"computer = {computer}")
    if user > computer:
    #print('You Win')
        if user == 2 and computer == 0:
            print('You Loose')
        else:
            print('You Win')
    elif user < computer:
        if user ==0 and computer == 2:
            print('You Win')
        else:
            print('You Loose')
    elif user == computer:
        print('You tied or DRAW')
print("\n")