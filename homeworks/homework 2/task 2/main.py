def divide_array(arr, x):
    if len(arr) == 0:
        return []

    val = arr[0]
    result = [[val]]
    line_sum = val
    i = 0

    for v in arr:
        if v > x:
            print("Number from array can not be bigger than x")
            return
        elif line_sum + v > x:
            result.append([v])
            i += 1
            line_sum = v
        else:
            result[i].append(v)
            line_sum += v

    return result


arr = [1, 2, 3, 4, 3, 4, 2, 3, 5]
print(divide_array(arr, 5))
