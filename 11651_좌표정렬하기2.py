n = int(input())
lst = []
for i in range(n):
    A, B = map(int,input().split())
    lst.append([A, B])

lst.sort(key = lambda x: (x[1], x[0]))

for i in lst:
    print(i[0],i[1])