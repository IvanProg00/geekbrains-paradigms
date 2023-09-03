from typing import List


def binary_search(nums: List[int], num: int) -> int:
    left = 0
    right = len(nums)

    while left < right:
        m = (left + right) // 2

        if nums[m] == num:
            return m
        elif nums[m] < num:
            left = m + 1
        else:
            right = m

    return -1


arr = [2, 5, 9, 14, 15, 28, 38, 45]
print(binary_search(arr, 2))
print(binary_search(arr, 5))
print(binary_search(arr, 9))
print(binary_search(arr, 14))
print(binary_search(arr, 15))
print(binary_search(arr, 28))
print(binary_search(arr, 38))
print(binary_search(arr, 45))

print(binary_search(arr, 36))
print(binary_search(arr, 12))
