# Day 4 - Beginner - Randomisation and Python Lists

<details>
<summary>

## Exercise 1 - Heads or Tails
File: [heads_or_tails.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_4/heads_or_tails.py)
</summary>

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g. 1 means Heads 0 means Tails

Example Output
```
Heads
```
or
```
Tails
```
</details>

<details>
<summary>

## Exercise 2 - Banker Roulette
File: [banker_roulette.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_4/banker_roulette.py)
</summary>

You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the `choice()` function.

Line 8 splits the string `names_string` into individual names and puts them inside a List called `names`. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

Example Input
```
Angela, Ben, Jenny, Michael, Chloe
```
Note: notice that there is a space between the comma and the next name.

Example Output
```
Michael is going to buy the meal today!
```
Hint:

You might need the help of the `len()` function.
</details>

</details>

<details>
<summary>

## Exercise 3 - Treasure Map
File: [treasure_map.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_4/treasure_map.py)
</summary>

You are going to write a program that will mark a spot with an `X`.

In the starting code, you will find a variable called `map`.

This `map` contains a nested list. When `map` is printed this is what the nested list looks like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code `print(f"{row1}\n{row2}\n{row3}")` to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Now it looks a bit more like the coordinates of a real map:

<img src="https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/dcf3f486-3ca7-40e2-8c2c-3e7ed90ea071/Co-ordinates_oggjzg+copy.png" width="450"/>

<br>

Your job is to write a program that allows you to mark a square on the map using a two-digit system. 

The first digit in the input will specify the column (the position on the horizontal axis).

The second digit in the input will specify the row number (the position on the vertical axis). 

So an input of 23 should place an X at the position shown below:

<img src="https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/67152b41-0349-4387-81ad-896f9c069c48/Day+4+Treasure+Map+Updated.png" width="700"/>

<br>

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "x". Remember that your nested list `map` actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

Example Input 1
column 2, row 3 would be entered as:
```
23
```
Example Output 1
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```
Example Input 2
column 3, row 1 would be entered as:
```
31
```
Example Output 2
```
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

Hint
1. Remember that Lists start at index 0!
2. `map` is just a variable that contains a nested list. It's not related to the map function in Python.
3. Remember that nested lists are accessed from out to in. So if `list=[[A,B,C],[E,F,G]]` then `E = list[1][0]`
4. Check that you haven't accidentally added extra spaces and the X is a capital X with a single quote around it.
Correctly formatted:
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```
vs. 

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']
```
</details>

<details>
<summary>

### Project: Rock Paper Scissors
File: [rock_paper_scissors.py](https://github.com/codenvibes/100DaysofCode/blob/master/Day_4/rock_paper_scissors.py)
</summary>

Make a rock, paper, scissors game.

Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

- How you will store the user's input.
- How you will generate a random choice for the computer.
- How you will compare the user's and the computer's choice to determine the winner (or a draw).
- And also how you will give feedback to the player.
</details>