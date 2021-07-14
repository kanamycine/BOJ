n = int(input())
lst = []
for i in range(n):
    lst.append(input())
set_list = []
x = list(set(lst))

sort_list = []
for i in range(len(x)):
    sort_list.append((len(x[i]), x[i]))
res = sorted(sort_list)
for i in range(len(res)):
    print(res[i][1])