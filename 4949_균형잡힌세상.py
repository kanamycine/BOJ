str = list(input())
stk = []
res = ""
for i in range(len(str)):
    if str[i] == '(' or str[i] == '[':
        stk.append(str[i])
    
    if str[i] == ')':
        if len(stk) == 0:
            res = "no"
            break
        elif stk[-1] == "(":
            stk.pop()
        
    elif str[i] == ']':
        if len(stk) == 0 :
            res = "no"
            break
        elif stk[-1] == "[":
            stk.pop()

if res == "no" or len(stk) != 0:
    res = "no"
else:
    if len(stk) == 0:
        res = "yes"
print(res)