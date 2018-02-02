def mergeSort(alist):
    if len(alist) > 1:
        midpos = len(alist) // 2
        lefthalf = alist[:midpos]
        righthalf = alist[midpos:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i, j, k = 0


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
