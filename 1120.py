A,B = map(str, input().split())
length = []
length.append(len(A))
length.append(len(B))
blen = max(length)
res = []

def sub(A,B):
    global key
    global string 
    string = []
    key = A
    if len(A) < len(B):
        key = B
        string.append(A + key[-1])
        string.append(key[0] + A)
    else:
        string.append(B + key[-1])
        string.append(key[0] + B)
    return string
    

def compare(A, B):
    cnt = 0
    for i in range(blen):
        if A[i] != B[i]:
            cnt += 1 
    return cnt

res.append(compare(sub(A,B)[0], B))
res.append(compare(sub(A,B)[1], B))
print(min(res))