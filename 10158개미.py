w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) // w
y = (q + t) // h

if x % 2 ==0:
    p = (p+t)%w
else:
    p = w - ((p+t) % w)
    
if y % 2 ==0:
    q = (q+t)%h
else:
    q = h - ((q+t) % h)
    
print('{} {}'.format(p,q))