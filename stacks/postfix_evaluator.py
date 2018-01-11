import math
from tokens.token_type import Tokens
from operators import Operators

class PostfixEvaluator:

    def solve(self, postfix_tokens):
        """ Given a list of tokens ordered by postfix notation, this method will return the evaluation """

        number_stack = []
        
        for token in postfix_tokens:
            if token.type == Tokens.OPERATOR:

                if len(number_stack) < 2:
                    error = SyntaxError()
                    error.offset = token.str_position
                    error.msg = "SyntaxError: Operator: [{}], at string position: {}".format(token.value, error.offset)
                    raise error

                right = number_stack.pop()
                left = number_stack.pop()

                result = self.__result_factory(left, right, token.value)
                number_stack.append(result)

            elif token.type == Tokens.NUMBER:
                number_stack.append(token.value)

        return number_stack.pop()

    
    def __result_factory(self, left, right, operator):
        
        if operator == Operators.ADD:
            return left + right

        elif operator == Operators.SUBTRACT:
            if left is None:
                return -right
            elif right is None:
                return -left
            else:
                return left - right

        elif operator == Operators.MULTIPLY:
            return left * right

        elif operator == Operators.DIVIDE:
            return left / right

        elif operator == Operators.POWER:
            return math.pow(left, right)

        elif operator == Operators.MOD:
            return math.fmod(left, right)

        else:
            raise Exception("Unknown Operator")



