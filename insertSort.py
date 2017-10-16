def insertSort(alist):
    for i in range(1, len(alist)):
        currentValue = alist[i]
        position = i
        while position > 1 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentValue
    return alist


print(insertSort([1, 152, 4, 6, 66, 7]))
