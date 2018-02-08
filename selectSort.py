def select_sort_asc(alist):
    length = len(alist)
    for i in range(length - 1):
        maxpos = 0
        for j in range(1, length - i):
            if alist[j] > alist[maxpos]:
                maxpos = j

        alist[length - 1 - i], alist[maxpos] = alist[maxpos], alist[length - 1 -
                                                                    i]
    return alist


def select_sort_des(alist):
    length = len(alist)
    for i in range(length - 1):
        maxpos = i
        for j in range(i + 1, length):
            if alist[j] > alist[maxpos]:
                maxpos = j
        alist[i], alist[maxpos] = alist[maxpos], alist[i]

    return alist


print(select_sort_asc([1, 4, 56, 43, 5, 66]))
print(select_sort_des([1, 4, 56, 43, 5, 66]))
