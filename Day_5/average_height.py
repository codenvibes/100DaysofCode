# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
for height in student_heights:
    total_height += height

count = 0
for _ in student_heights:
    count += 1

average_height = round(total_height / count)
print(average_height)
#Write your code below this row 👇