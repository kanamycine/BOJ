n = int(input())
res = 0
for i in range(0,n+1):
    lst = list(str(i))
    if i < 100: 
        res += 1
    elif int(lst[1]) - int(lst[0]) == int(lst[2]) - int(lst[1]):
        res += 1
print(res-1)

