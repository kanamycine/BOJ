n = int(input())
res = 0


for i in range(1, n+1): 
    lst = list(map(int,str(i)))
    s = i + sum(lst)
    if (s == n):
        res = i
        break

print(res)