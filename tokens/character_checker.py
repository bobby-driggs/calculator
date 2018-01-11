import re

class CharacterChecker:
    ReIsOperator = re.compile('\+|-|\*|/|\^|%')
    ReIsLetter = re.compile('[a-zA-Z]')

    def is_operator(self, string):
        return bool(CharacterChecker.ReIsOperator.match(string))

    def is_letter(self, string):
        return bool(CharacterChecker.ReIsLetter.match(string))

    def is_number(self, string):
        return string.replace(".", "", 1).isdigit()

    def is_decimal(self, string):
        return string == "."

    def is_left_parenthesis(self, string):
        return string == "("

    def is_right_parenthesis(self, string):
        return string == ")"