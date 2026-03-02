import random
import words_list
import hangmandoll

Chosen_word = random.choice(words_list.fruits)
print ('\n')
# print(Chosen_word)
display = []
lives = 7

# for i in range(len(fruits)):
for letter in Chosen_word:
    display += '_'
print("Guess a Fruit name which has length: ", len(Chosen_word))
print("You have 7 Chances!")
print(display)
game_over = False
while not game_over:
    print('\n')
    guessed_letter = input("Guess a letter: ").lower()
    print('\n')
    for position in range(len(Chosen_word)):
        letter = Chosen_word[position]
        if letter == guessed_letter:
            # print(" match")
            display[position] = guessed_letter
            # print(display)
    print(display)
    if guessed_letter not in Chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("\n")
            print(f"The fruit is : '{Chosen_word}'.")
            print("You lose!!")
    if '_' not in display:
        game_over = True
        print("You win!!")
    print(hangmandoll.stages[lives])
    