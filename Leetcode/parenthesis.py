def ValidParenthesis(s):
    stack = []
    closeToopen = {")" : "(", "}" : "{", "]" : "["}
        
    for c in s:
        if c in closeToopen:
            if stack and stack[-1] == closeToopen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    if not stack:
        return True
    else:
        return False

print(ValidParenthesis("()[]{}"))