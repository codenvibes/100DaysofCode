# Day 5 - Beginner - Python Loops

<details>
<summary>

## Exercise 1 - Average Height
File: [average_height.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_5/average_height.py)
</summary>

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

**Important** You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input
```
156 178 165 171 187
```
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output
```
171
```
</details>

<details>
<summary>

## Exercise 2 - High Score
File: [high_score.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_5/high_score.py)
</summary>

You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
```
78 65 89 86 55 91 64 89
```
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
```
The highest score in the class is: 91
```
Hint:

Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?
</details>

<details>
<summary>

## Exercise 3 - Adding Even Numbers
File: [adding_even_numbers.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_5/adding_even_numbers.py)
</summary>

You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Hint:
There are quite a few ways of solving this problem, but you will need to use the `clear` function in any of the solutions.
</details>

<details>
<summary>

## Exercise 4 - FizzBuzz
File: [fizz_buzz.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_5/fizz_buzz.py)
</summary>

You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

  And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

e.g. it might start off like this:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
.... etc.
```
Hint:

1. Remember your answer should start from 1 and go up to and including 100.
2. Each number/text should be printed on a separate line.
</details>

<details>
<summary>

## Day 5 Project: Create a Password Generator
File: [password_generator.py]()
</summary>

The program will ask:
```
How many letters would you like in your password?
```
```
How many symbols would you like?
```
```
How many numbers would you like?
```
The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

### Easy Version (Step 1)

Generate the password in sequence. If the user wants 
* 4 letters
* 2 symbols and
* 3 numbers

then the password might look like this: 

```
fgdx$*924
```
You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first. 

### Hard Version (Step 2)

When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
```
x$d24g*f9
```
And every time you generate a password, the positions of the symbols, numbers, and letters are different. 
</details>