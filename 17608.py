n = int(input())
stack = []
res = []
for i in range(n):
    tmp = int(input())
    if stack == []:
        stack.append(tmp)
    while stack[-1] < tmp:
        stack.pop()
        stack.append(tmp)
