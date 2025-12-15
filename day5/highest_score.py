student_score = [88,67,57,99,67,88,95,56,63,63]

# total_score = sum(student_score)

# print(total_score)

sum = 0
max = 0
for score in student_score:
    if score >= max:
        max = score
    sum += score

print(sum)
print(max)