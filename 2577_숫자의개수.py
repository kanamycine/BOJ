a = int(input())
b = int(input())
c = int(input())

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = a * b * c
num_list = list(map(int, str(result)))

for i in range(len(str(result))):
    arr[num_list[i]] += 1
#
for i in range(len(arr)):
    print(arr[i])
