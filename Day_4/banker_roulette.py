# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_people = len(names)
random_person = random.randint(0, num_people -1)

person_who_will_pay = names[random_person]
print(person_who_will_pay + " is going to buy the meal today!")
