sound_list = list(map(int, input().split()))
n = 0
for i in range(7):
    if sound_list[i+1] == sound_list[i] + 1:
        n += 1
    elif sound_list[i+1] == sound_list[i] - 1:
        n -= 1
if n == 7:
    print('ascending')
elif n == -7:
    print('descending')
else:
    print('mixed')