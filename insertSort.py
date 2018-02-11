def insertion_sort_asc(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        position = i
        while position > 0 and alist[position - 1] > current:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = current
    return alist


def insertion_sort_des(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        position = i
        while position > 0 and alist[position - 1] < current:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = current
    return alist


print(insertion_sort_asc([1, 152, 4, 6, 66, 7]))
print(insertion_sort_des([1, 152, 4, 6, 66, 7]))
