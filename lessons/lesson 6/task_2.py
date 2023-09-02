def sum_squares(nums):
    res = 0

    for n in nums:
        if n % 2 == 0:
            res += n**2

    return res


print(sum_squares([5, 6, 8, 1, 2, 3]))
