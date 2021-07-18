s = list(input())
n = int(input())

cur = len(s)
for i in range(n):
    lst = []
    lst = list(map(str, input().split()))
    if len(lst) == 2:
        s.insert(cur+1,lst[1])
        print("list =", s)
    elif lst[0] == 'L':
        if cur == 0 :
            cur = 0
        else: cur -= 1
        print("cur =" ,cur)
    else:
        cur += 1
        print("cur =" , cur)
print(s)
