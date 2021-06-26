a = input()
b = input()
c = input()

n = int(a) * int(b) * int(c)
lst = [0,0,0,0,0,0,0,0,0,0]
for i in str(n):
    lst[int(i)] += 1
for i in lst:
    print(i)