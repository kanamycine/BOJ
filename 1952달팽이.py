A, B = map(int, input().split())
arr = [[0] * A for _ in range(B)]
cnt = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x =0
y =0
d = 0
while cnt < A*B:
    x = x+dx[d]
    y = y+dy[d]
    if x < 0 or x > A-1 or B < 0 or B > B-1 or arr[x][y]:
        d = (d + 1) % 4 
        cnt += 1
    arr[x][y] += 1

print(cnt)