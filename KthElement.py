# Brett Bittola
# 1/21/2024
# CS 325
# Takes two sorted arrays and takes the Kth element of the combined array


def kthElement(arr1, arr2, k):
    """Finds the Kth element of a combined list of two sorted arrays"""
    # base case, when one array is empty, take the kth element of the other array.
    m = len(arr1)
    n = len(arr2)

    if m == 0:
        return arr2[k-1]
    elif n == 0:
        return arr1[k-1]

    # find the midpoint of both arrays
    mid1 = m // 2
    mid2 = n // 2

    # if k is larger than the sum of the two midpoints, remove the lower half of one of the arrays, reduce k by the
    # number of elements being removed, and call the function again on the new arrays
    if (mid1 + mid2 + 1) < k:
        if arr1[mid1] > arr2[mid2]:
            k = k-mid2-1
            arr2 = arr2[mid2+1:]
            return kthElement(arr1, arr2, k)
        else:
            k = k-mid1-1
            arr1 = arr1[mid1+1:]
            return kthElement(arr1, arr2, k)

    # if k is larger than the sum of the two midpoints, remove the upper half of one of the arrays and call the function
    # again
    else:
        if arr1[mid1] > arr2[mid2]:
            arr1 = arr1[:mid1]
            return kthElement(arr1, arr2, k)
        else:
            arr2 = arr2[:mid2]
            return kthElement(arr1, arr2, k)
