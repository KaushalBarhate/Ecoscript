from sly import Parser
from lexer import EcoScriptLexer

class EcoScriptParser(Parser):
    tokens = EcoScriptLexer.tokens

    def __init__(self):
        self.names = { }
        self.energy = 0
        self.carbon_footprint = 0
        self.output = "" # Store the print statements


    @_('statements statement')
    def statements(self, p):
        pass

    @_('statement')
    def statements(self, p):
        pass

    @_('NAME ASSIGN expr ";"')
    def statement(self, p):
        self.names[p.NAME] = p.expr
        self.energy += 1
        self.carbon_footprint += 0.1

    @_('NAME "(" expr ")" ";"')
    def statement(self, p):
        if p.NAME == 'PRINT':
            print(p.expr)
            self.output += str(p.expr) + "\n"
            self.energy += 1
            self.carbon_footprint += 0.05
        else:
            print(f"Unknown function '{p.NAME}'")
    

    #array and if 

    # If statement without else
    @_('IF "(" condition ")" "{" statements "}"')
    def statement(self, p):
        if p.condition(): # Call the lambda function
            p.statements
        self.energy += 1
        self.carbon_footprint += 0.1
    
    # If-Else statement
    @_('IF "(" condition ")" "{" statements "}" ELSE "{" statements "}"')
    def statement(self, p):
        if p.condition(): # Call the lambda function
            p.statements0
        else:
            p.statements1
        self.energy += 1
        self.carbon_footprint += 0.1

    
    # While loop
    @_('WHILE "(" condition ")" "{" statements "}"')
    def statement(self, p):
        while p.condition():
            p.statements
        self.energy += 1
        self.carbon_footprint += 0.1

     

    @_('NAME ASSIGN "[" exprs "]" ";"')
    def statement(self, p):
        self.names[p.NAME] = p.exprs
        self.energy += 1
        self.carbon_footprint += 0.1

    @_('exprs "," expr')
    def exprs(self, p):
        return p.exprs + [p.expr]

    @_('expr')
    def exprs(self, p):
        return [p.expr]

    @_('expr LT expr')
    def condition(self, p):
        return lambda: p.expr0 < p.expr1
    
    @_('expr GT expr')
    def condition(self, p):
        return lambda: p.expr0 > p.expr1


    #end

    @_('expr PLUS term')
    def expr(self, p):
        self.carbon_footprint += 0.01
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        self.carbon_footprint += 0.01
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        self.carbon_footprint += 0.02
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        self.carbon_footprint += 0.02
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        self.carbon_footprint += 0.005
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        self.carbon_footprint += 0.005
        return int(p.NUMBER)

    @_('NAME')
    def factor(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print("Undefined name '%s'" % p.NAME)
            return 0
