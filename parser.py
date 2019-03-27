from ast import AST

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens

    
    def parse(self):
        for i in range(0,len(self.tokens)):
            for token in self.tokens[i]:
                if(token == "print"):
                    AST().printToScreen(self.tokens[i][2])
                elif (token.startswith("$")):
                    AST().setVariable(self.tokens[i])
                    
                


        

