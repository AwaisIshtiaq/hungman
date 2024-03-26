import random
from hangman_word import word_list
from hangman_art import stages,logo
from replit import clear



chosen_word = random.choice(word_list)

word_length = len(chosen_word)

display = []

lives = 6
print(logo)

for i in range(word_length):
    display += "_"


end_games = False

while not end_games:
    guess = input("chosse a word : ").lower()
    clear()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_games = True
            print("Youse Lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_games  = True
        print("You Win.")

    print(stages[lives])