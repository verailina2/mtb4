def find_digit_in_number(number, index1, index2, digit):
    min_index, max_index = sorted([index1, index2])

    if digit in number[min_index:max_index + 1]:
        return True
    else:
        return False


number = input('Введите число:')
index1 = int(input('Введите первый индекс:'))
index2 = int(input('Введите второй индекс:'))
digit = input('Введите цифру, которую нужно искать в заданном числе:')

result = find_digit_in_number(number, index1, index2, digit)
if result:
    print(f"Цифра {digit} есть в числе {number} между индексами {min_index} и {max_index}")
else:
    print(f"Цифры {digit} нет в числе {number} между индексами {min_index} и {max_index}")
