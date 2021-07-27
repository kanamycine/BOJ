n = int(input())
lst = list(map(int, input().split()))
stk = []
tower = []

for i in range(n):
    while stk:
        if stk[-1][1] > lst[i]:
            tower.append(stk[-1][0]+1)
            break
        else:
            stk.pop()
    if not stk:
        tower.append(0)
    stk.append([i, lst[i]])

for i in range(len(tower)):
    print(tower[i], end=" ")