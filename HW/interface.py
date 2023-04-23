from inputdata import *

def interface():
    print("""1 - Добавление
    2 - Поиск
    3 - Вывод на экран
    4 - Удаление записи
    5 - Изменить запись""")
    ask = int(input())
    if ask == 1:
        input_data()
    elif ask == 2:
        search()
    elif ask == 3:
        print_data()
    elif ask == 4:
        delite_contact()
    elif ask == 5:
        change_contact()
    else:
        print("Нет такой команды")