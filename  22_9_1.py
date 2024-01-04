def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

def sort_list(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

input_str = input("Введите последовательность чисел через пробел: ")
sequence = list(map(int, input_str.split()))

number = int(input("Введите число: "))

sorted_sequence = sort_list(sequence)
position = binary_search(sorted_sequence, number)

print("Позиция элемента в отсортированной последовательности:", position)