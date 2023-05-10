def find_digit_in_number():
    number = input('Введите число:')
    index1 = int(input('Введите первый индекс:'))
    index2 = int(input('Введите второй индекс:'))
    digit = input('Введите цифру, которую нужно искать в заданном числе:')
    min_index, max_index = sorted([index1, index2])
    if digit in number[min_index:max_index + 1]:
        print(f"Цифра {digit} есть в числе {number} между индексами {min_index} и {max_index}")
    else:
        print(f"Цифры {digit} нет в числе {number} между индексами {min_index} и {max_index}")


print(find_digit_in_number())

# Да, действительно следующее задание – представить решение задачи в виде функции.
# Но конечно мы бы хотели убрать конструкции с input из функции (либо вынести их, либо удалить)
# и зафиксировать возвратное значение из фукцнии через return как True или False
# Также в функцию надо передать параметры)
