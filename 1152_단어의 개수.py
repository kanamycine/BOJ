#str = list(map(str, input().split(" ")))
str = input()
res = str.split(" ")


if res[0] == '':
    del res[0]

if res[-1] == '':
    del res[-1]

print(len(res))
