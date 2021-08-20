import sys
from collections import deque

dq = deque()

def push_front(x):
    dq.insert(0, x)
def push_back(x):
    dq.append(x)
def pop_front():
    if dq:
        print(dq.popleft())
    else:
        print(-1)
def pop_back():
    if dq:
        print(dq.pop())
    else: 
        print(-1)
def size():
    print(len(dq))
def empty():
    if dq:
        print(0)
    else:
        print(1)
def front():
    if dq:
        print(dq[0])
    else:
        print(-1)
def back():
    if dq:
        print(dq[-1])
    else:
        print(-1)


n = int(input())
for i in range(n):
    input_l = sys.stdin.readline().split()
    if input_l[0] == "push_front":
        push_front(input_l[1])
    elif input_l[0] == "push_back":
        push_back(input_l[1])
    elif input_l[0] == "pop_front":
        pop_front()
    elif input_l[0] == "pop_back":
        pop_back()
    elif input_l[0] == "size":
        size()
    elif input_l[0] == "empty":
        empty()
    elif input_l[0] == "front":
        front()
    elif input_l[0] == "back":
        back()
        

    