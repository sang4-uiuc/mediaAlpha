ops = {"+": 1, "-": 1, "/":2, "*":2, "empty": 0}

# checks if the two paranthesis at start and end are redundant
def ifRedundant(left, right, start, end, s, redun):
    if left is None and right is None:
        redun.append(start)
        redun.append(end)
        return
    else:
        if left is None:
            left = "empty"
            left
        if right is None:
            right = "empty"
        x = findLowest(start, end, s)
        if x is None:
            redun.append(start)
            redun.append(end)
            return
        # special case where the paranthesis are both necessary when there's subtraction before and inside the paranthesis
        if left == "-" and (s[x] == '-' or s[x] == '+'):
            return
        if ops[s[x]] < ops[left] or ops[s[x]] < ops[right]:
            return
        else:
            redun.append(start)
            redun.append(end)
            return

# finds the lowest operator inside the two paranthesis
def findLowest(start, end, s):
    lowest = []
    flag = False
    for i in range(start+1, end):
        if s[i] == "(":
            flag = True
        elif s[i] in ops and flag == False:
            lowest.append((i, ops[s[i]]))
        elif s[i] == ")":
            flag = False
    if len(lowest) == 0:
        return None
    else:
        low = min(lowest, key=lambda x: x[1])
        return low[0]

# finds the first operator to the left of the starting paranthesis
def findLeft(index, s):
    left = None
    for i in range(index, -1, -1):
        if s[i] in ops:
            left = s[i]
            break
    return left

# finds the first operator to the right of the ending paranthesis
def findRight(index, s):
    right = None
    for i in range(index, len(s)):
        if s[i] in ops:
            right = s[i]
            break
    return right

# finds the corresponding ending paranthesis
def findEndBracket(index, s):
    stack = []
    for i in range(index, len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            stack.pop()
            if len(stack) == 0:
                return i

# returns a simplified version without unnecessary paranthesis
def removeParenthesis(s):
    redun = []
    for i in range(len(s)):
        if s[i] == "(":
            start = i
            end = findEndBracket(i, s)
            left = findLeft(start, s)
            right = findRight(end, s)
            ifRedundant(left, right, start, end, s, redun)
    if len(redun) == 0:
        return s
    else:
        simplified = ""
        for i in range(len(s)):
            if i in redun:
                continue
            else:
                simplified += s[i]
        return simplified

while True:
    s = input("Enter the expression: ")
    if s == "exit":
        break
    else:
        print(removeParenthesis(s))
