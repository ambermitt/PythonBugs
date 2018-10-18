###################################################################
# balloon.py
###################################################################
This code calculates the total volume of a list of balloon radii,
and prints this value. Then, we pop balloons at certain indices of 
the list of balloon radii and print the new volume after popping
them. 

When the main() from this file is run, it should successfully 
output the following:

>>>main()
8067.609934418589
825.1916703429188

###################################################################
# quadratic.py
###################################################################
This code prints the roots of a quadratic equation given a specific
user input of a(variable)^2 + b(variable) + c, where a, b, and c are
constant coefficients and (variable) is any character. Note, each 
coefficient MUST be an integer. If left blank, the code does NOT 
assume the coefficient is 1. 

When the main() is run, a sucessful sample interaction is:

>>> main()
Equation: 3t^2 + 3t - 5
t  =  0.8844373104863458
t  =  -1.8844373104863459
>>> main()
Equation: 1x^2 - 5x + 6
x  =  3.0
x  =  2.0
>>> main()
Equation: 20y^2 + 10y - 30
y = 1.0
y = -1.5

###################################################################
# unhex.py
###################################################################
When main() is run, it will keep prompting the user for a input.
If the input is a valid positive hexadecimal integer (lowercase), 
the program will output that number in decimal. 
Otherwise, it will output -1.
Enter "quit" or "q" to quit.

Sample Interaction:
>>>main()
> 0xfff
4095
> 12345678
305419896
> monkey
-1

###################################################################
# minesweeper.py
###################################################################
This code is for making the game board for Minesweeper,
a game where the player is given a grid of blank squares.
Uncovering a square reveals either the number of adjacent squares 
with land mines in them, or a land mine (represented by 'X' here). 
If they uncover a mine, they lose.
The goal is to uncover every square that doesn't contain a mine.

When the main() from this file is run, it should successfully 
output just the underlying board for a game of Minesweeper.

Sample output (mine locations will be randomized):
1 X 2 X 1 0 0 0 1 1 2 X 1 0 0 0 0 0 0 0 
1 2 3 2 1 0 0 1 2 X 2 1 1 0 0 0 0 0 1 1 
2 3 X 1 0 0 0 1 X 2 1 0 1 1 1 0 0 0 1 X 
X X 3 3 2 1 0 1 2 2 1 0 2 X 2 0 0 1 2 2 
3 3 2 X X 3 2 1 1 X 1 0 3 X 3 0 0 1 X 1 
X 1 2 3 5 X X 1 1 1 1 0 2 X 2 0 1 3 3 2 
1 1 2 X 4 X 3 1 0 0 1 1 3 2 2 0 1 X X 2 
0 1 3 X 3 1 1 1 1 1 1 X 2 X 1 0 1 3 4 X 
1 2 X 3 2 1 0 1 X 1 1 1 3 2 2 0 0 2 X 4 
1 X 3 3 X 1 0 2 2 2 0 1 2 X 1 0 1 4 X X 
2 2 2 X 2 1 0 1 X 1 0 1 X 3 2 0 1 X X 4 
X 2 2 1 1 0 0 1 1 2 1 2 2 X 1 0 1 3 X 3 
2 X 1 0 1 1 1 0 0 1 X 1 1 1 1 0 0 2 3 X 
1 1 1 0 1 X 1 0 0 1 1 1 0 0 0 0 0 2 X 3 
1 2 2 2 2 2 2 1 1 0 0 0 0 0 0 0 0 3 X 4 
1 X X 4 X 2 1 X 1 0 0 0 1 1 1 0 0 3 X X 
1 3 4 X X 2 1 1 1 0 0 0 1 X 1 0 0 2 X 3 
0 1 X 3 2 1 0 1 1 1 1 2 3 2 1 0 0 1 2 2 
0 2 2 2 0 0 0 1 X 1 1 X X 2 0 0 0 0 1 X 
0 1 X 1 0 0 0 1 1 1 1 3 X 2 0 0 0 0 1 1 

###################################################################
# spaghetti.py
###################################################################
Table of sample correct outputs for spaghetti(x):
 x  | spaghetti(x)
-------------------------
 0  | 0.0
 1  | 0.01745240647289035
 2  | 0.0348994967736821
 3  | 0.05233595634963419
10  | 0.1736481780176426
20  | 0.3420201439949603
30  | 0.5000000009252338

