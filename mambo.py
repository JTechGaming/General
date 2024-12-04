# pip install random_word
from random_word import RandomWords

r = RandomWords()

word = r.get_random_word()

max_word_length = int(input("Choose a maximum word length: "))

while len(word) > max_word_length:
    word = r.get_random_word()

wordguess = [] and word
currentguess = []

for char in word:
    wordguess.append(char)
    currentguess.append("_")

lives = 5

difficulty = input("Choose a difficulty from:\n- Easy\n- Normal\n- Hard\n: ")
if difficulty == "Easy":
    lives = 10
if difficulty == "Normal":
    lives = 5
if difficulty == "Hard":
    lives = 3

attempts = 0
while lives != 0:
    print("Current guess:", ''.join(currentguess))
    attempts = attempts + 1
    guessed = input("Enter a letter/word\n: ")
    if guessed == word:
        print("You WIN!")
        print("In:", attempts, "attempts")
        lives = 0
    elif guessed in wordguess:
        if len(guessed) == 1:
            print("Correct letter,", guessed, "guessed")
            for i in range(len(wordguess)):
                if wordguess[i]==guessed:
                    currentguess[i] = guessed
        else:
            print("You can only input one letter, or the entire word!")
    else:
        lives = lives - 1
        print("Wrong,", lives, "lives are left")
    contains = False
    for letter in currentguess:
        if letter == "_":
            contains = True
    if contains == False:
        print("You WIN!")
        print("In:", attempts, "attempts")
        lives = 0

print("The word was:", word)