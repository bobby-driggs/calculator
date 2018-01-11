from tokens.token import Token
from tokens.token_type import Tokens


class TokenFactory:

    def create_number(self, value, str_position):
        return Token(Tokens.NUMBER, value, str_position)

    def create_operator(self, value, str_position):
        return Token(Tokens.OPERATOR, value, str_position)

    def create_left_parenthesis(self, str_position):
        return Token(Tokens.LEFT_PARENTHESES, "(", str_position)

    def create_right_parenthesis(self, str_position):
        return Token(Tokens.RIGHT_PARENTHESES, ")", str_position)
