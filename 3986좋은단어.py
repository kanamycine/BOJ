n = int(input())
cnt = 0

for i in range(n):
    stk =[]
    lst = list(input())
    while lst:
        if not stk:
            stk.append(lst.pop())
        else:
            if lst[-1] == stk[-1]:
                stk.pop()
                lst.pop()
            else:
                stk.append(lst.pop())
    if not stk : cnt += 1
print(cnt)