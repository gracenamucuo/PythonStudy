#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#二分查找 基于一个有序数组
def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        mid = int(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
        return  None
print(binary_search([1,4,56,67],5))

#快排
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + pivot + quicksort(greater)

print(quicksort([1,4,5,23,3]))



















































