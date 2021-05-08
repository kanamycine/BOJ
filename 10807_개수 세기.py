t = int(input())
lst = list(map(int, input().split()))
n = int(input())
cnt = 0
for i in range(len(lst)):
    if lst[i] == n:
        cnt += 1

print(cnt)
