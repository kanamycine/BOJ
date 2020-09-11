a, b = map(int, input().split())
arr = [[1]*(b + 2)] + [[1] + [0] * b + [1] for _ in range(a)] + [[1]*(b+2)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
i = 1
j = 1
d = 0
cnt = 0
t = a*b
while True:
    if not arr[i][j]:
        arr[i][j] = 1
        t -= 1
        if t == 0:
            break
        i += di[d]
        j += dj[d]
    else:
        i -= di[d]
        j -= dj[d]
        d = (d+1) % 4
        cnt += 1
        i += di[d]
        j += dj[d]
print(cnt)
