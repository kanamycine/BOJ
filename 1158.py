from collections import deque
N, M = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)

ans = []
for i in range(N-1):
    for j in range(M-1):
        q.append(q.popleft())
    ans += [q.popleft()]

ans += [q[0]]
print('<'+', '.join(map(str, ans)) + '>')
