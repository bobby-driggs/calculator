class Operators:
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "^"
    MOD = "%"
    L_PARENTHESIS = "("
    R_PARENTHESIS = ")"

    PRECIDENTS = {}
    PRECIDENTS[L_PARENTHESIS] = 1
    PRECIDENTS[R_PARENTHESIS] = 1
    PRECIDENTS[ADD] = 2
    PRECIDENTS[SUBTRACT] = 2
    PRECIDENTS[MULTIPLY] = 3
    PRECIDENTS[DIVIDE] = 3
    PRECIDENTS[MOD] = 3
    PRECIDENTS[POWER] = 4 

    ALL = [ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER, MOD]

    def get_regex_string(self):
        return "{}|{}|{}|{}|{}|{}".format(Operators.ADD, Operators.SUBTRACT, Operators.MULTIPLY, Operators.DIVIDE, Operators.POWER, Operators.MOD)