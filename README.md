## Calculator
Evaluates mathematical strings, formatted in infix notation, passed in as a command line argument.
## Dependencies
No outside dependencies.
## Usage
```
$ python calculate.py "1 + 2 * 3 + 4"
11.0
```
Turn debug on, with the ```-d``` flag. With debug on, the application will also print the tokens for both the entered infix notation, as well as the postfix notion, before printing the answer.
```
$ python calculate.py -d  "1 + 2 * 3"
Number          => 1.0
Operator        => +
Number          => 2.0
Operator        => *
Number          => 3.0
1.0 + 2.0 * 3.0
Number          => 1.0
Number          => 2.0
Number          => 3.0
Operator        => *
Operator        => +
1.0 2.0 3.0 * +
7.0
```
### Operators
Here is a list of allowed **binary** operators:
•	    ADD: "+"
•	    SUBTRACT: "-"
•	    MULTIPLY: "*"
•	    DIVIDE: "/"
•	    POWER: "^"
•	    MOD: "%"
•	    L_PARENTHESIS: "("
•	    R_PARENTHESIS: ")"

**NOTE:** Unary operators, including the negation operator, are not supported.
