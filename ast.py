from global_shared import vars

class AST():
    def __init__(self):
        pass
    
    # Print Function
    def printToScreen(self,tokens):
        string = ""
        isString = 0
        isVar = 0
        #print(tokens)
        for char in list(tokens):
            if char != "\"":
                string += char
                if char == "$":
                    isVar = 1
            else:
                isString = 1
                
        # Check if its a variable and set it's value
        if(isVar == 1):
            string = vars[string.strip("$")]

        # Check if its an expression and get it's value
        try:
            if(isString == 0):
                string = eval(string)
        except:
            pass 
        print(string)

    # Set Variables
    def setVariable(self,tokens):
        var_name = ""
        var_value = ""
        for token in tokens:
            if(token.startswith("$")):
                var_name = token.strip("$")
            elif(token == "="):
                pass
            else:
                var_value = token
        if var_value.startswith("\""):
            var_value = var_value.strip("\"")
        vars[var_name] = var_value
