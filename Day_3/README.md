# Day 3 Beginner - Control Flow and Logical Operators

<details>
<summary>

## Exercise 1 - Odd or Even 
</summary>

Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is **even** because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is **odd** because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The **modulo** is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

`6 ÷ 2 = 3` with no remainder.

therefore: `6 % 2 = 0`

5 ÷ 2 = 2 x 2 + 1, remainder is 1.

therefore: `5 % 2 = 1`

14 ÷ 4 = 3 x 4 + 2, remainder is 2.

therefore: `14 % 4 = 2`

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input 1
```
43
```
Example Output 1
```
This is an odd number.
```
Example Input 2
```
94
```
Example Output 2
```
This is an even number.
```
</details>


<details>
<summary>

## Exercise 2 - BMI 2.0
</summary>

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.
- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.

<img src="https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36" />

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

<img src="https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/6653a739-6bc2-4d53-b566-67f5c0b32849/BMI+Image+Small.jpeg" width=200/>

Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. **underweight, normal weight, overweight, obese, clinically obese**.

Example Input
```
weight = 85
height = 1.75
```
Example Output
```
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.
```
Hint
1. Try to use the exponent operator in your code.
1. Remember to round your result to the nearest whole number.
1. Make sure you include the words in bold from the interpretations.
</details>

<details>
<summary>

## Exercise 3 - Leap Year 
</summary>

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input 1
```
2400
```
Example Output 1
```
Leap year.
```
Example Input 2
```
1989
```
Example Output 2
```
Not leap year.
```
<img src="https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB%2BfSUsY4wcQhqwC%2B0p0urDu29Xu08KHTiYLD4JPE2%2B8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh%2BLw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL%2BmdA4Kb7s%2Br18ZIKLycaSLMERn2%2BI4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq%2BCIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i%2B53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE%2BTz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4%2BtMr9GahYzglGkjOsBnCv3%2BWKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq%2B20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG%2BZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4%2BdXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq%2BMRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt%2BbAL2s%2Bk5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO%2Bb9jyp%2BLwMvf"/>
</details>