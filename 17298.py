n = int(input())
lst = list(map(int, input().split()))
stack = []
res = [-1 for _ in range(n)]
for i in range(n):
    while len(stack) != 0 and lst[stack[-1]] < lst[i]:
        res[stack.pop()] = lst[i]
    stack.append(i)
for j in range(len(res)):
    print(res[j], end=" ")
