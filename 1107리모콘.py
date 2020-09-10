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
print(a)
for x in a:
    broken[x] = True
print(broken)
def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else: 
            return 1
    l = 0
    while c > 0:
        if broken[c%10]:
            return 0 
        l += 1
        c //= 10
    return l

ans = abs(n-100)
for i in range(0, 1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-n)
        if ans > 1 + press:
            ans = l + press
print(ans)