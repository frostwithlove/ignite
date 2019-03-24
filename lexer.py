from ops_parens import *

class Lexer():
    def __init__(self,data):
        self.data=data
        self.tokens=[]

    @staticmethod
    def _compose(tokens):
        composed_tokens = []
        list_of_tokens = []
        for token in tokens:
            if(token != ";"):
                composed_tokens.append(token)
            else:
                list_of_tokens.append(composed_tokens)
                composed_tokens = []
        return(list_of_tokens)


    def lex(self):
        token = ""
        flag = 0
        for char in list(self.data):
            if char == '\"' and flag == 0 :
                flag = 1
            elif char == '\"' and flag == 1:
                flag = 0
            if char in paren:
                if flag == 0 :
                    self.tokens.append(token)
                    self.tokens.append(char)
                    token = ""
                else:
                    token += char
            elif char == " " and flag !=1 :
                pass
            elif char == "\n" :
                pass
            else:
                token += char  

        self.tokens = Lexer._compose(self.tokens)
        return self.tokens

        
        
        
