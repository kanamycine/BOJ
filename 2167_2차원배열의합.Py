A, B = map(int, input().split())
lst = [list(map(int, input().split()))for _ in range(A)]

n = int(input())
for i in range(n):
    a,b,c,d = map(int,input().split())
    res = 0
    for j in range(a-1, c):
        for k in range(b-1, d):
            res += lst[j][k]
    print(res)