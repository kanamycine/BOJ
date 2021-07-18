lst = []
odd_lst = []
for i in range(7):
    x = int(input())
    lst.append(x)
for i in lst:
    if i % 2 == 1:
        odd_lst.append(i)
if len(odd_lst) == 0:
    print(-1)
else: 
    print(sum(odd_lst))
    print(min(odd_lst))