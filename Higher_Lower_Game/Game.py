import random
import game_art
import game_database
import os

print(game_art.Game_Logo)
score =0

def display_accountinfo(Account):
    name = Account["name"]
    description = Account["description"]
    Country = Account["country"]
    return (f"{name}, {description}, {Country}")

def check_answer(guess, followers_1, followers_2):
    if followers_1 < followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
        

# continue_Flag = True
# while continue_Flag:
#     Account_1 = random.choice(game_database.data)
#     Account_2 = random.choice(game_database.data)
#     print(f"Compare 1 : {display_accountinfo(Account_1)}")
#     print(Account_1["follower_count"])
#     print(game_art.Vs)
#     print(f"Compare 2 : {display_accountinfo(Account_2)}")
#     print(Account_2["follower_count"])
#     guess = int(input("Who has more followers? Type 1 or Type 2: "))
#     followers_count_1 = Account_1["follower_count"]
#     followers_count_2 = Account_2["follower_count"]
#     print(followers_count_1)
#     print(followers_count_2)

#     is_correct = check_answer(guess, followers_count_1, followers_count_2)
#     if is_correct:
#         score +=1
#         print(f"You are Right🎆!, Your score is : {score}")
#         print("\n")
#     else:
#         print(f"You are Wrong!, Your final score is : {score}")
#         continue_Flag = False




        ###############  2nd Account Becomes first Account


Account_1 = random.choice(game_database.data)

continue_Flag = True
while continue_Flag:
    Account_2 = random.choice(game_database.data)
    while Account_1 == Account_2:                           #####   to stop to get the same values 
        Account_2 = random.choice(game_database.data)
    print(f"Compare 1 : {display_accountinfo(Account_1)}")
    print(Account_1["follower_count"])
    print(game_art.Vs)
    print(f"Compare 2 : {display_accountinfo(Account_2)}")
    print(Account_2["follower_count"])
    guess = int(input("Who has more followers? Type 1 or Type 2: "))
    followers_count_1 = Account_1["follower_count"]
    followers_count_2 = Account_2["follower_count"]
    print(followers_count_1)
    print(followers_count_2)
    is_correct = check_answer(guess, followers_count_1, followers_count_2)
    os.system('cls')
    print(game_art.Game_Logo)
    if is_correct:
        score +=1
        print("\n")
        print(f"You are Right🎆!, Your score is : {score}")
        Account_1 = Account_2

    else:
        print(f"You are Wrong!, Your final score is : {score}")
        continue_Flag = False