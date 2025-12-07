height = input("Enter Height (Cm): ")
weight = input("Enter Weight (Kg): ")

height = float(height)/100

bmi = float(weight) / (float(height) ** 2)

print(bmi)
