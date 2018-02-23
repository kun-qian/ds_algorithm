#!usr/bin/env python3
# -*- coding: utf-8 -*-


def quick_sort_in_place(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_pos = partition(alist, first, last)
        quick_sort_helper(alist, first, split_pos)
        quick_sort_helper(alist, split_pos + 1, last)


def partition(alist, first, last):
    pivot = alist[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] < pivot:
            left_mark = left_mark + 1

        while left_mark <= right_mark and alist[right_mark] > pivot:
            right_mark = right_mark - 1

        if left_mark >= right_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    return right_mark


def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        left_list = []
        right_list = []
        pivot_list = []
        for v in alist:
            if v < pivot:
                left_list.append(v)
            elif v > pivot:
                right_list.append(v)
            else:
                pivot_list.append(v)
        return quick_sort(left_list) + pivot_list + quick_sort(right_list)


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# quick_sort_in_place(a_list)
print(quick_sort(a_list))
