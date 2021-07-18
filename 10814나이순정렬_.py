n = int(input())
lst = []
for i in range(n):
    A, B = map(str, input().split())
    age = int(A)
    lst.append((age, B))
lst.sort(key = lambda x: (x[0]))

for i in lst:
    print(i[0], i[1])



