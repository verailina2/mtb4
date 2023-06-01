

input_string = input()        # входная строка

def baby_age(input_string):
    length_string = len(input_string)       # длина входной строки
    result = ''                             # результат из входной строки (возраст)
    i = 0                                   # счетчик
    while i < length_string:
        current_symbol = input_string[i]
        if '0' <= current_symbol <= '9':
            result += str(current_symbol)
        i += 1
    return result or 'None'

print(baby_age(input_string))

if __name__ == '__main__':
    pass