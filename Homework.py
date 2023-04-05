def get_divisible_numbers(numbers, divisor):
    result = []
    for number in numbers:
        if number % divisor == 0:
            result.append(number)
    return result

# Примеры использования функции:
print(get_divisible_numbers([1, 2, 3, 4, 5, 6], 2))  # [2, 4, 6]
print(get_divisible_numbers([0, 1, 2, 3, 4, 5, 6], 4))  # [0, 4]
print(get_divisible_numbers([0], 4))  # [0]
print(get_divisible_numbers([1, 3, 5], 2)) 