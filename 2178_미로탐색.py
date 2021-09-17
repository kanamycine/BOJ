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

# BFS는 큐의 front 부분을 pop하여 진행해야 한다. 
# 이 문제로 골치를 썪은 이유는. rear에서 pop 이 진행 됐기 때문에,
# 넓이 우선 탐색이 아닌 깊이 우선 탐색이 되어버렸다.
# 결국 다른 방향의 경로가 마지막 지점에서 만날 때에는, 1이 아닌 값이 들어가 있어서 아래 구문이 진행되지 않는다.
# 최단,최소라는 요구사항이 있을 때는 BFS를 우선적으로 고민해본다.

# while que:
#     a, b = que[0][0], que[0][1]
#     del que[0]
#     for i in range(4):
#         x = a + dx[i]
#         y = b + dy[i]
#         if 0 <= x < A and 0 <= y < B and arr[x][y] == "1":
#             que.append([x, y])
#             arr[x][y] = arr[a][b] + 1