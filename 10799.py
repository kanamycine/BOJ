lst = list(input())
stack = []
res = 0
for j in range(len(lst)):
    if lst[j] == '(':
        stack.append('(')
    else:
        if lst[j-1] == '(':
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1
print(res)
