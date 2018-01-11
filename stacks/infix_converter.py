from tokens.token_type import Tokens
from operators import Operators

class InfixConverter:

    def to_postfix(self, tokens):
        """ Converts a list of tokens ordered by infix notation, to a list of tokens ordered by postfix notation """
        
        postfix_stack = []

        operator_stack = []

        for token in tokens:
            if token.type == Tokens.NUMBER:
                postfix_stack.append(token)
                
            elif token.type == Tokens.LEFT_PARENTHESES:
                operator_stack.append(token)

            elif token.type == Tokens.RIGHT_PARENTHESES:
                top_token = operator_stack.pop()
                while top_token.type != Tokens.LEFT_PARENTHESES:
                    postfix_stack.append(top_token)
                    top_token = operator_stack.pop() 

            elif token.type == Tokens.OPERATOR:
                while len(operator_stack) > 0 and Operators.PRECIDENTS[operator_stack[-1].value] >= Operators.PRECIDENTS[token.value]:
                    postfix_stack.append(operator_stack.pop())

                operator_stack.append(token)
            else:
                pass

        while len(operator_stack) > 0:
            postfix_stack.append(operator_stack.pop())

        return postfix_stack
