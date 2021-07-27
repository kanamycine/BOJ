n = int(input())
stck=[]
for i in range(n):
    lst = list(map(str,input().split()))
    if lst[0] == 'push':
        stck.append(lst[1])
    elif lst[0] == 'top':
        if len(stck) == 0:
            print(-1)
        else:
            print(stck[-1])
    elif lst[0] == 'size':
        print(len(stck))
    elif lst[0] == 'empty':
        if len(stck) == 0:
            print(1)
        else:
            print(0)
    elif lst[0] == 'pop':
        if len(stck) == 0:
            print(-1)
        else:
            print(stck.pop())

