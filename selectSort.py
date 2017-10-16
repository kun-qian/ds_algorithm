def selectSortAsc(alist):
    for i in range(len(alist) - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if alist[j] > alist[maxpos]:
                maxpos = j
        alist[i], alist[maxpos] = alist[maxpos], alist[i]
    return alist

def selectSortDesc(alist):
    for i in range(len(alist)):
        maxpos = i
        for j in range(i + 1, len(alist)):
            if alist[j] > alist[maxpos]:
                maxpos = j
        alist[i], alist[maxpos] = alist[maxpos], alist[i]
    return alist

print(selectSortAsc([1, 152, 4, 6, 66, 7, 3]))
print(selectSortDesc([1, 152, 4, 6, 66, 7, 3]))