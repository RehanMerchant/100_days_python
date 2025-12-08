import sys

print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepporoni = input("Do you want peporoni on the pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0

if size == "S":
    price=15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Wrong input")
    sys.exit()

if pepporoni == "Y":
    if price == 15:
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1


print(f"Your total bill would be ${price}")