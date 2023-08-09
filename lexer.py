from sly import Lexer

class EcoScriptLexer(Lexer):
    tokens = { NAME, NUMBER, ASSIGN, PLUS, MINUS, TIMES, DIVIDE,IF, ELSE, FOR, WHILE, LBRACKET, RBRACKET,  LT, GT}
    ignore = ' \t'
    literals = { ';', '(', ')' , '{', '}', ','}

    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ASSIGN = r':='
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    NUMBER = r'\d+'
    NAME['if'] = IF
    NAME['else'] = ELSE
    NAME['for'] = FOR
    NAME['while'] = WHILE
    LBRACKET = r'\['
    RBRACKET = r'\]'
    LT = r'<'
    GT = r'>'

    # Ignored pattern
    ignore_newline = r'\n+'
    ignore_comment = r'\#.*'

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
