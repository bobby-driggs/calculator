class Calculator:

    def __init__(self, tokenizer, infix_converter, postfix_evaluator, is_debug):
        self.tokenizer = tokenizer
        self.infix_converter = infix_converter
        self.postfix_evaluator = postfix_evaluator
        self.is_debug = is_debug

    def process(self, string):
        """ Evaluates an infix string, and returns the result """

        tokens = self.tokenizer.parse(string)
        self.__print_tokens(tokens)

        postfix_tokens = self.infix_converter.to_postfix(tokens)
        self.__print_tokens(postfix_tokens)

        return self.postfix_evaluator.solve(postfix_tokens)

    def __print_tokens(self, tokens):
        if not self.is_debug:
            return

        for token in tokens:
            print("{:<15} => {}".format(token.type, token.value))

        print(" ".join(map(lambda t: str(t.value), tokens)))

