def selectSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if alist[j] > alist[maxpos]:
                maxpos = j
        alist[i], alist[maxpos] = alist[maxpos], alist[i]
    return alist


print(selectSort([1, 152, 4, 6, 66, 7, 3]))
