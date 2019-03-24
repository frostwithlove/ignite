

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens

    
    def parse(self):
        for i in range(0,len(self.tokens)):
            for token in self.tokens[i]:
                if(token == "print"):
                    string = ""
                    for char in list(self.tokens[i][2]):
                        if char != "\"" :
                            string += char
                    try :
                        string = eval(string)
                    except:
                        pass                 
                    print(string)


        

