arr = [[0]*101 for _ in range(101)]

tc = int(input())

for t in range(1, tc+1):
    F, S = list(map(int, input().split()))

    for i in range(F,F+10):
        for j in range(S, S+10):
            arr[i][j] = 1

cnt = 0
for line in arr:
    if 1 in line:
        cnt += sum(line)
print(cnt)     