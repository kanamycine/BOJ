lst = [0]
cnt = 0
res = []
for _ in range(4):
    a, b = map(int, input().split())
    lst.append(a)
    lst.append(b)

for i in range(1,9):
    if i % 2 == 0:
        cnt += lst[i]
    else:
        cnt -= lst[i]
    res.append(cnt) 

print(max(res))