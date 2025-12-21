import random

word_list = ["hero","ballon","don"]
random_word = random.choice(word_list)
print(random_word)


letter = input("Enter a letter: ").lower()
print(letter)


for l in random_word:
    if l == letter:
        print("Right")
    else:
        print("Wrong")