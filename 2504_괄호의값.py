def do_or_die():
    stk = []
    for i in s:
        if i == ")" or i == "]":
            if len(stk) == 0:
                return False
        if i == "(" or i == "[":
            stk.append(i)
        if i == ")":
            if stk[-1] == "(":
                stk.pop()
            else: 
                stk.append(")")
        elif i == "]":
            if stk[-1] == "[":
                stk.pop()
            else: 
                stk.append("]")
    if stk:
        return False
    else :
        return True

s = input()
stk = []
tmp = 1
if do_or_die():
    for i in s:
        if i == "(" or i == "[":
            stk.append(i)
        if i == ")":
            if stk[-1] == "(":
                stk.pop()
                stk.append(2)
            elif isinstance(stk[-1], int):
                tmp *= stk[-1]
                stk.pop()
                while stk[-1] != "(":
                    tmp += stk.pop()
                stk.pop()
                stk.append(tmp * 2)
            tmp = 1
        if i == "]":
            if stk[-1] == "[":
                stk.pop()
                stk.append(3)
            elif isinstance(stk[-1], int):
                tmp *= stk[-1]
                stk.pop()
                while stk[-1] != "[":
                    tmp += stk.pop()
                stk.pop()
                stk.append(tmp * 3)
            tmp = 1
    print(sum(stk))
else:
    print(0)