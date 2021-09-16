A, B = map(int, input().split())
arr = [list(input()) for _ in range(A)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

que = [(0,0)]
arr[0][0] = 1

while que:
    x, y = que[0][0], que[0][1]
    del que[0]
    for i in range(4):
        nx, ny = x+dx[i] , y+dy[i]
        
        if 0 <= nx < A and 0 <= ny < B:
            if arr[nx][ny] == "1":
                que.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1



print(arr)
print(arr[A-1][B-1])







# while que:
#     a, b = que[0][0], que[0][1]
#     del que[0]
#     for i in range(4):
#         x = a + dx[i]
#         y = b + dy[i]
#         if 0 <= x < A and 0 <= y < B and arr[x][y] == "1":
#             que.append([x, y])
#             arr[x][y] = arr[a][b] + 1