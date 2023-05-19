# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Calculate the number of years left
years_left = 90 - int(age)
# Calculate the number of months left
months_left = years_left * 12
# Calculate the number of weeks left
weeks_left = years_left * 52
# Calculate the number of months left
days_left = years_left * 365

# print("You have", days_left, "days,", weeks_left, "weeks, and", months_left, "months left.")

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
