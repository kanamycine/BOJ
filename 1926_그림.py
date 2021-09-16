def BFS(x,y):
    w = 1
    que = [(x,y)]
    while que:
        x, y = que.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < A and 0 <= ny < B:
                if arr[nx][ny] == 1 and not visit[nx][ny]:
                    w += 1
                    visit[nx][ny] = 1
                    que.append((nx,ny))
    return w

A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(A)]
visit = [[0 for _ in range(B)] for _ in range(A)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0
res = 0
for i in range(A):
    for j in range(B):
        if arr[i][j] == 1 and not visit[i][j]:
            cnt += 1
            visit[i][j] = 1
            res = max(res, BFS(i,j))


print(cnt)
print(res)