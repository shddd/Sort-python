import random as rd

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )

def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]

        cursor = i - 1

        while cursor >= left and array[cursor] > key_item:

            array[cursor + 1] = array[cursor]
            cursor -= 1

        array[cursor + 1] = key_item

    return array

def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])
            array[start:start + len(merged_array)] = merged_array
        size *= 2
    return array


#Just for testing
A = []
for i in range (0, 500):
    A.append(rd.randint(0, 1234))
timsort(A)
for i in range(0, 499):
    if(A[i]>A[i+1]):
        print("False")
