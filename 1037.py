n = int(input())
list = list(map(int, input().split()))

res = 1
for i in list:
    res = max(list) * min(list)
print(res)
