a, b = map(int,input().split())

minu = (a * 60) + b
bojung = minu - 45 
h = bojung // 60
m = bojung % 60
if h == -1:
    h = 23
print(h,m)