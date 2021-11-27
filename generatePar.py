def make(string):
    return "(" + string + ")" 
def generateParenthesis(n: int):
    res = []
    string = ""
    for i in range(n):
        string = make(string)
    string = list(string)
    
print (generateParenthesis(3))