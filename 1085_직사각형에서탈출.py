x, y, w, h = map(int,input().split())
lst = []
lst.append(w-x)
lst.append(h-y)
lst.append(w-(w-x))
lst.append(h-(h-y))
print(min(lst))

#x, y, w, h = list(map(int, input().split()))
#print(min([x, y, w - x, h - y]))