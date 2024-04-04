# Input a list of student scores
student_scores = input('Type list of student scores in format xx xx xx xx\n').split()

for score_index in range(0, len(student_scores)):
    student_scores[score_index] = int(student_scores[score_index])

# Write your code below this row 👇
highest = 0
for score in student_scores:
    if score > highest:
        highest = score

print(f'The highest score in the class is: {highest}')
