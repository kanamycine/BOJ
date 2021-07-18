lst = list(map(int, input().split()))
set_lst = set(lst)
if len(set_lst) == 3:
    print(max(set_lst)*100)
elif len(set_lst) == 1:
    print(10000 + (lst[0]*1000))
else:
    if lst[0] == lst[1]:
        print((lst[0]*100) + 1000)
    elif lst[0] == lst[2]: 
        print((lst[0]*100) + 1000)
    else:
        print((lst[1]*100) + 1000)