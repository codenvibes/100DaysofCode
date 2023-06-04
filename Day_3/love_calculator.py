# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# count TRUE
count_T = name1.lower().count('t') + name2.lower().count('t')
count_R = name1.lower().count('r') + name2.lower().count('r')
count_U = name1.lower().count('u') + name2.lower().count('u')
count_E = name1.lower().count("e") + name2.lower().count('e')

# Count LOVE
count_L = name1.lower().count('l') + name2.lower().count('l')
count_O = name1.lower().count('o') + name2.lower().count('o')
count_V = name1.lower().count('v') + name2.lower().count('v')

# Totals
total1 = count_T + count_R + count_U + count_E
total2 = count_L + count_O + count_V + count_E

love_score = int(str(total1) + str(total2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")