A, B = map(int, input().split())
arr2 = [[1]*(B+2)] + [[1]+[0] * B + [1] for _ in range(A)] + [[1]*(B+2)]
arr = [[0] * B for _ in range(A)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x = 0
y = 0
d = 0
cnt = 0
# for i in range(A*B):
#     x = x + dx[d]
#     y = y + dy[d]
#     arr[x][y] += 1
#     if x < 0 or x == B - 1 or y == A - 1 or y < 0 or arr[x][y] == 1:
#         d = (d + 1) % 4
#         arr[x][y] += 1
#         cnt += 1
print(arr)
print(cnt)
print(arr2)
