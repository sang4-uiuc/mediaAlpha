ops = {"+", "-", "/", "*"}

def removeParenthesis(s):
    paranthesis = []
    operator = []
    for i in range(len(s)):
        if s[i] in ops:
            operator.append(i)
        elif s[i] == "(":
            paranthesis.append(i)
    print(paranthesis)
    print(operator)

removeParenthesis("(1/2)")