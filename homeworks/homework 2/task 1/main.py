def search_path(arr, start, end):
    if len(arr) == 0 or len(arr[0]) == 0:
        return None

    start_row, start_col = start
    end_row, end_col = end
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    visited = [[False for _ in range(len(arr[i]))] for i in range(len(arr))]

    def dfs(row, col, history):
        if (
            row < 0
            or row >= len(arr)
            or col < 0
            or col >= len(arr[row])
            or visited[row][col]
            or arr[row][col] == 1
        ):
            return None
        history = history.copy()

        visited[row][col] = True
        history.append((row, col))

        if row == end_row and col == end_col:
            return history

        for sum_row, sum_col in directions:
            new_history = dfs(row + sum_row, col + sum_col, history)
            if new_history is not None:
                return new_history

        return None

    return dfs(start_row, start_col, [])


# arr = [
#     [0, 0, 0, 0],
#     [0, 1, 1, 0],
#     [0, 1, 1, 1],
#     [0, 0, 1, 0],
#     [0, 0, 0, 0],
# ]
# start = (0, 0)
# end = (4, 3)

arr = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
]
start = (2, 2)
end = (3, 3)

path = search_path(arr, start, end)
if path:
    print(path)
else:
    print("Path not found")
