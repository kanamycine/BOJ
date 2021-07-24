n = int(input())
stck = [] 
res = 0
for i in range(n):
    k = int(input())
    if k == 0:
        if len(stck) == 0:
            continue
        else:
            stck.pop(-1)
    else:
        stck.append(k)
res = sum(stck)
print(res)