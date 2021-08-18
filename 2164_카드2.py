from collections import deque
firstinput = int(input())
dq = deque()
for i in range(1, firstinput + 1):
    dq.append(i)


def func(n):
    if n == 0:
        dq.popleft()
    elif n == 1:
        dq.append(dq.popleft())

n = -1
while(len(dq) != 0 ):
    if len(dq) == 1:
        print(dq[0])
        break
    if n == 1:
        n = -1
    n += 1
    func(n)




