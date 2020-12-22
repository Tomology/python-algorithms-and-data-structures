"""
QUICK SORT 

Time Complexity
Best Case       O(n log n)
Worst Case      O(n^2)

Space Complexity
O(log n)

"""


def quickSort(arr, left=0, right=None):
    if right == None:
        right = len(arr) - 1

    if left < right:
        pivotIndex = pivot(arr, left, right)

        # left
        quickSort(arr, left, pivotIndex - 1)

        # right
        quickSort(arr, pivotIndex + 1, right)

    print(arr)
    return arr


"""
PIVOT HELPER FUNCTION
Uses the element at the 'start' index as the pivot.
All elements in the list that are less than the pivot will be moved to the left of the pivot.
All elements in the list that are greater than the pivot will be moved to the right of the pivot.
The pivot element will be at the correct index once function finishes executing.
The index of the pivot element is returned.
"""


def pivot(arr, start, end):

    pivot = arr[start]
    swapIdx = start

    for i in range(start + 1, end + 1):
        if pivot > arr[i]:
            swapIdx += 1
            arr[swapIdx], arr[i] = arr[i], arr[swapIdx]

    arr[start], arr[swapIdx] = arr[swapIdx], arr[start]

    return swapIdx


quickSort([4, 2, 6, -2, 0, 23, -10, -3, 54, 0])
