from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    arr = []
    l_index = 0
    r_index = 0

    while l_index < len(sorted_left) and r_index < len(sorted_right):
        if sorted_left[l_index] <= sorted_right[r_index]:
            arr.append(sorted_left[l_index])
            l_index += 1
        else:
            arr.append(sorted_right[r_index])
            r_index += 1

    if l_index < len(sorted_left):
        arr.extend(sorted_left[l_index:])
    elif r_index < len(sorted_right):
        arr.extend(sorted_right[r_index:])

    return arr


print(merge_sort([5, 4, 3, 2, 1]))
print(merge_sort([8, 3, 2, 8, 5, 3, 9, 4, 2]))
