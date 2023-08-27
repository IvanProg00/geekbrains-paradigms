class BubbleSort:
    def sort(self, numbers):
        for i in range(0, len(numbers) - 1):
            for j in range(0, len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


class InsertionSort:
    def sort(self, numbers):
        for i in range(1, len(numbers)):
            val = numbers[i]
            j = i - 1

            while j >= 0 and numbers[j] > val:
                numbers[j + 1] = numbers[j]
                j -= 1

            numbers[j + 1] = val


class SortStrategy:
    def __init__(self, sort_algo):
        self.sort_algo = sort_algo

    def sort(self, numbers):
        self.sort_algo.sort(numbers)


bubble_sort = BubbleSort()
insertion_sort = InsertionSort()
sort_strategy = SortStrategy(bubble_sort)

numbers = [8, 3, 2, 1, 4, 8, 3, 4, 6, 5]
sort_strategy.sort(numbers)
print(numbers)


sort_strategy.sort_algo = insertion_sort
numbers = [8, 3, 2, 1, 4, 8, 3, 4, 6, 5]
sort_strategy.sort(numbers)
print(numbers)
