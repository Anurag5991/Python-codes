def SimplifyPath(path):
    stack = []
    cur = ""

    for i in path + '/':
        if i == "/":
            if cur == "..":
                if stack: stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            cur = ""
        else:
            cur += i
    return "/" + "/".join(stack)

print(SimplifyPath("/../"))