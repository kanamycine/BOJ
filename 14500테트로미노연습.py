arr = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
    ]
total = 0
tlst = []
dx = [0,1,0,1]
dy = [0,0,1,1]

for i in range(2):
    for j in range(2):
        for k in range(4):
            x, y = i+dx[k], i+dy[k]
            if 0 <= x < 3 and 0 <= y < 3:
                total += arr[x][y]
        tlst.append(total)
        total = 0
            
print(tlst)
