# Алгоритм 9

# 1. Напишите алгоритм сортировки Шелла (shell sort)
# Рассмотрите, как алгоритм работает в отладчике (debug)

# Дополнительно
# 2. Создайте функцию min/max, которая использует алгоритм сортировки написанный выше 


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def min_value(arr):
    sorted_lst = shell_sort(arr)
    return sorted_lst[0]


def max_value(arr):
    sorted_lst = shell_sort(arr)
    return sorted_lst[-1]


lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
print(shell_sort(lst))
print(min_value(lst))
print(max_value(lst))
