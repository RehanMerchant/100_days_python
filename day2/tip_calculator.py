print("Welcome to tip calculator!")
bill = input("What was the total bill? $")
bill = float(bill)

tip_rate=input("How much tip would you like to give? 10, 15, 20? ")
tip_rate=int(tip_rate)

split = input("How many people to split the bill? ")
split = int(split)

tip = bill * (tip_rate/100)
bill = bill + tip

each_pay = round(bill / split,2)

print(f"Eac person should pay: ${each_pay}")
