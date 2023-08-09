# run_ecoscript.py
from interpreter import EcoScriptInterpreter

def run_ecoscript_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    interpreter = EcoScriptInterpreter()
    interpreter.interpret(code)

if __name__ == "__main__":
    import sys
    run_ecoscript_file(sys.argv[1])
