import sys

n = int(input())
q = []

def push(x):
    q.insert(0, x)
def pop():
    if q :
        print(q.pop())
    else :
        print(-1)
def size():
        print(len(q))
def empty():
    if q :
        print(0)
    else :
        print(1)
def front():
    if q :
        print(q[-1])
    else:
        print(-1)
def back():
    if q :
        print(q[0])
    else:
        print(-1)

for i in range(n):
    input_l = sys.stdin.readline().split()
    if input_l[0] == 'push':
        push(int(input_l[1]))
    elif input_l[0] == 'pop':
        pop()
    elif input_l[0] == 'size':
        size()
    elif input_l[0] == 'empty':
        empty()
    elif input_l[0] == 'front':
        front()
    elif input_l[0] == 'back':
        back()
        
