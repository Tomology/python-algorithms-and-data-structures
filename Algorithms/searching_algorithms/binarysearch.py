"""
BINARY SEARCH
Binary Search can only be used on sorted arrays. 
Time Complexity:    O(log n)
Space Complexity:   O(1) 
"""


def binarysearch(arr, elem):
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = (min + max) // 2

        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            min = mid + 1
        else:
            max = mid - 1

    return -1


binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 123], 33)
