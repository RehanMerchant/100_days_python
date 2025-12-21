import random

word_list = ["hero","ballon","don"]
random_word = random.choice(word_list)
print(random_word)

placeholder = ""

for pos in range (0,len(random_word)):
    placeholder += "_"

print(placeholder)

guess_letter = input("Guess a Letter: ")

display = ""

for letter in random_word:
    if letter == guess_letter:
        display+=letter
    else:
        display+="_"


print (display)
