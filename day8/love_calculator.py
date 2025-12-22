def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()
    first = 0
    last = 0

    for letter in combined_name:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            first += 1

        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            last += 1

    res = int(str(first) + str(last))
    print(res)

calculate_love_score("Kanye West", "Kim Kardashian")
