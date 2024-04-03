# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum_of_height = 0
count_of_height = 0
for height in student_heights:
  sum_of_height += height
  count_of_height += 1

print(f"total height = {sum_of_height}")
print(f"number of students = {count_of_height}")
print(f"average height = {round(sum_of_height/count_of_height)}")