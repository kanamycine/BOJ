tc = int(input())
for t in range(tc):
    n = input()
    stack = []
    res = "YES"
    for i in n:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                res ="NO"
                break
            elif stack.pop() == '(':
                res = "YES"
            else:
                res = "NO"
    if len(stack) > 0:
        res = "NO"
        
    print(res)