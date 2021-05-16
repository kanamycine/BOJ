lst = list(map(str, input().split()))
res1 = lst[0][2]+lst[0][1]+lst[0][0]
res2 = lst[1][2]+lst[1][1]+lst[1][0]
if res1 > res2:
    print(res1)
elif res1 < res2:
    print(res2)
