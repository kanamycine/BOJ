lst = []
for i in range(0,21):
    lst.append(i)

for i in range(10):
    A, B = map(int,input().split())
    tmp = list(reversed(lst[A:B+1]))
    for j in range(len(tmp)):
        lst[A+j] = tmp[j]
lst.remove(0)
for i in lst:
    print(i, end = " ")