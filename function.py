def get_quarter(month):
    if 1 <= month <= 3:
        quarter = 1
    elif 4 <= month <= 6:
        quarter = 2
    elif 7 <= month <= 9:
        quarter = 3
    elif 10<= month <= 12:
        quarter = 4
    else:
        print("введенный номер месяца некорректен")
        return None
    return quarter

month = int(input("Введите номер месяца (от 1 до 12):"))
quarter = get_quarter(month)
if quarter:
    print("№ квартала:", quarter)