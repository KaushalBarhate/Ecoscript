from parser import EcoScriptParser
from lexer import EcoScriptLexer

class EcoScriptInterpreter:
    def __init__(self):
        self.parser = EcoScriptParser()
        self.lexer = EcoScriptLexer()

    def interpret(self, text):
        self.parser.parse(self.lexer.tokenize(text))
        print("Energy Consumed:", self.parser.energy)
        print("Carbon Footprint:", self.parser.carbon_footprint)
        output = self.parser.output
        output += "Energy Consumed: " + str(self.parser.energy) + "\n"
        output += "Carbon Footprint: " + str(self.parser.carbon_footprint)
        return output

if __name__ == '__main__':
    interpreter = EcoScriptInterpreter()
    while True:
        try:
            text = input('ecoscript > ')
        except EOFError:
            break
        if text:
            interpreter.interpret(text)
