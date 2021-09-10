str = input()
stk = []
tmp = 0
res = 0
for i in str:
    print(stk)
    if len(stk) == 0:
        res += tmp
    if i == "(" or i == "[":
            stk.append(i)
    elif i == ")":
        if stk[-1] == "(":
            del stk[-1]
            if tmp == 0:
                stk.append(2)
            else:
                stk.append(tmp * 2)
                del stk[-1]
                stk.append(tmp)
                tmp = 0
        else: 
            while(stk[-1] != "("):
                if tmp == 0:
                    tmp += stk[-1]
                    del stk[-1]
                else: 
                    tmp *= stk[-1]
                    del stk[-1]
                    stk.append(tmp)
    elif i == "]":
        if stk[-1] == "[":
            del stk[-1]
            if tmp == 0 :
                stk.append(3)
            else:
                stk.append(tmp * 3)
                del stk[-1]
                stk.append(tmp)
                tmp = 0
        else:
            while(stk[-1] != "["):
                if tmp == 0:
                    tmp += stk[-1]
                    del stk[-1]
                    stk.append(tmp)
                else: 
                    tmp *= stk[-1]
                    del stk[-1]
                    stk.append(tmp)
print(stk)