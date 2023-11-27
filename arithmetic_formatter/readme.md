
# Arithmetic Formatter

This is the first project in the "Scientific Coomputing with Python" course with FreeCodeCamp. The challenge is to create a function that will except a list of calculations as strings, and the output should be formatted on screen as shown below. There is a second optional parameter that will be "False" by default, but when set to "True", it needs to show the answer as well on the output. 

### Output with only a list as a parameter
`arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])`

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

### Ouput with list as the first paramater and True as the second parameter

`arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)`
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
## Rules for the project

    1. The list used for the parameter can contain a maximum of 5 items. For more items, display: "Error: Too many problems."
    2. Operators can only be + or -. For any other operators, display: "Error: Operator must be '+' or '-'"
    3. Ensure that operands are valid numbers, otherwhise display: "Error: Numbers must only contain digits."
    4. Maximum characters for a number is 4. For more characrters, display:
    
Assumptions made:
There are always only 2 operands. So never 3 numbers for a single calculation.
There is always a space before and after the operator.


## Link to project
[Free Code Camp - Ccientific Computing with python](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)


## How to run the functions
Ensure the arithmetic_arranger.py file is in the same folder as the main.py folder.
Run the main.py file. It imports the "validations" and "arithmetic_arranger" functions.
Change the calculations list to different values to view different variations. Toggle the show_answer parameter in the arithmetic_arranger function between True and 
False to view the output with and without the answers respectively.