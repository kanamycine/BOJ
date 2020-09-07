import sys
n = int(input())
res = []
for _ in range(n):
    res.append(int(sys.stdin.readline()))


def sol():
    stack = []
    for s in res[::-1]:
        if not stack or stack[-1] < s:
            stack.append(s)
    return len(stack)


print(sol())
