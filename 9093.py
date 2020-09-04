tc = int(input())
for t in range(tc):
    n = list(map(str, input().split()))
    stack = []

    for i in range(len(n)):
        res=[]
        for j in range(len(n[i])):
            stack.append(n[i][j])
        for k in range(len(stack)):
            res.append(stack.pop())
        a = ''.join(res)
        print(a, end=' ')
    