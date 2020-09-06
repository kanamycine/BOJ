tc = int(input())
lst = []
for i in range(tc):
    n = int(input())
    if n != 0:
        lst.append(n)
    else:
        lst.pop()
total = sum(lst)
print(total)
