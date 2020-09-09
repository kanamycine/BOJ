'''
5457
3
6 7 8

6
'''
n = int(input())
m = int(input())
broken = [False] * 10
if m > 0 :
    a = list(map(int, input().split()))
else:
    a = []
for x in a:
    broken[x] = True

def possible(c):
    