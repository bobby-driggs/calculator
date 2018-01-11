class Tokenizer:

    def __init__(self, character_checker, token_factory):
        self.character_checker = character_checker
        self.token_factory = token_factory
    
    def parse(self, string):
        """ Parses a string ordered by infix notation, and generates lexicon tokens """

        tokens = []

        if string is None or string == "":
            return tokens
        
        number_buffer = []

        for i, character in enumerate(string):
            if self.character_checker.is_number(character):
                number_buffer.append(character)

            elif self.character_checker.is_decimal(character):
                number_buffer.append(character)

            elif self.character_checker.is_left_parenthesis(character):
                operator_token = self.token_factory.create_left_parenthesis(i)
                tokens.append(operator_token)

            elif self.character_checker.is_right_parenthesis(character):
                if len(number_buffer):
                    self.__create_number_token(number_buffer, tokens, i)

                operator_token = self.token_factory.create_right_parenthesis(i)
                tokens.append(operator_token)

            elif self.character_checker.is_operator(character):
                if len(number_buffer):
                    self.__create_number_token(number_buffer, tokens, i)

                operator_token = self.token_factory.create_operator(character, i)
                tokens.append(operator_token)

            else:
                pass

        if len(number_buffer):
            self.__create_number_token(number_buffer, tokens, len(string) - 1)

        return tokens

    def __create_number_token(self, buffer, tokens, str_position):
        number_value = self.__convert_to_number(buffer)
        number_token = self.token_factory.create_number(number_value, str_position)
        tokens.append(number_token)
        buffer.clear()

    def __join_buffer(self, buffer):
        return "".join(buffer)

    def __convert_to_number(self, buffer):
        return float(self.__join_buffer(buffer))
