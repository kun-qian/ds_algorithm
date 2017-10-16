def binarySearch1(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpos = (first + last) // 2
        if item == alist[midpos]:
            found = True
        if item < alist[midpos]:
            last = midpos - 1
        if item > alist[midpos]:
            first = midpos + 1
    return found


def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = (len(alist) - 1)// 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch2(alist[:midpoint], item)
            else:
                return binarySearch2(alist[midpoint + 1:], item)


print(binarySearch2([1, 2, 3, 4, 5], 6))
