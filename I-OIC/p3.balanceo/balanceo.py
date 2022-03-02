import fileinput

def balanced(s):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    num = []
    check = False
    for c in s:
        if c in "{[(":
            stack.append(c)
            check = True
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        elif c not in "{[(":
            num.append(c)
        else:
            return "FALSE"
    if len(stack) == 0 and check:
        return "TRUE"
    else:
        return "FALSE"

for line in fileinput.input():
    print (balanced(line))