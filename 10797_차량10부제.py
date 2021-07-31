n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if i == n:
        cnt += 1
print(cnt)