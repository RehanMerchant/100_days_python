import random

word_list = ["hero","ballon","don"]
random_word = random.choice(word_list)
print(random_word)

placeholder = ""

for pos in range (0,len(random_word)):
    placeholder += "_"

print(placeholder)

display = ""
game_over = False
correct_letter = []

while not game_over:
    guess_letter = input("Guess a Letter: ").lower()

    display = ""

    for letter in random_word:
        if letter == guess_letter:
            display+=letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display+="_"


    print (display)
    if "_" not in display:
        game_over = True
        print("You Win")
