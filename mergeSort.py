def merge_sort_asc(alist):
    if len(alist) > 1:
        left_half = alist[:len(alist) // 2]
        right_half = alist[len(alist) // 2:]
        merge_sort_asc(left_half)
        merge_sort_asc(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1


a = [1, 4, 56, 43, 5, 66]
merge_sort_asc(a)
print(a)
