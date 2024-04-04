# Input a Python list of student heights
student_heights = input().split()
for index in range(0, len(student_heights)):
  student_heights[index] = int(student_heights[index])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum_of_height = 0
count_of_height = 0
for height in student_heights:
  sum_of_height += height
  count_of_height += 1

average_height = round(sum_of_height/count_of_height)
print(f"total height = {sum_of_height}")
print(f"number of students = {count_of_height}")
print(f"average height = {average_height}")