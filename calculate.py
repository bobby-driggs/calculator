import argparse

from tokens.character_checker import CharacterChecker
from tokens.token_factory import TokenFactory
from tokens.tokenizer import Tokenizer

from stacks.infix_converter import InfixConverter
from calculator import Calculator
from stacks.postfix_evaluator import PostfixEvaluator

parser = argparse.ArgumentParser(description="Process a string as a math equation")

parser.add_argument("equation", metavar="E", type=str, help="The string to process as an equation")
parser.add_argument("-d", "--debug", action="store_true", help="debug output verbosity")

args = parser.parse_args()

character_checker = CharacterChecker()
token_factory = TokenFactory()

tokenizer = Tokenizer(character_checker, token_factory)
infix_converter = InfixConverter()
postfix_evaluator = PostfixEvaluator()

calculator = Calculator(tokenizer, infix_converter, postfix_evaluator, args.debug)

try:
    result = calculator.process(args.equation)
    print("{}".format(result))
except SyntaxError as error:
    print(error.msg)
    if error.offset is not None:
        s = args.equation
        s = s[:error.offset + 1] + ']' + s[error.offset + 1:]
        s = s[:error.offset] + '[' + s[error.offset:]
        print(s)
