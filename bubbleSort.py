def bubble_sort_asc(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    return alist


def bubble_sort_des(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] < alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


print(bubble_sort_asc([3, 43, 1, 45, 67, 34]))
print(bubble_sort_des([3, 43, 1, 45, 67, 34]))
