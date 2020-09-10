cham = int(input())
lst = []
for _ in range(6):
    A, B = map(int,(input().split()))
    lst.append(B)

max1 = max(lst)
max1i = lst.index(max1)
max2 = min(
    lst[(max1i + 5) % 6] , 
    lst[(max1i + 7) % 6])

max2i = lst.index(max2)
max3 = lst[(max2i + 7) % 6]

max3i = lst.index(max3)
max4= lst[(max3i+7) % 6]

max4i = lst.index(max4)
max5= lst[(max4i+7) % 6]

max5i = lst.index(max5)
max6= lst[(max5i+7) % 6]


print(((max1 * max6) - (max3 * max4)) * cham)
