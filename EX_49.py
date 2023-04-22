"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""
def writing_person():
    name = input("Введите имя: ")
    lastname = input("Введите фамилию: ")
    surname = input("Введите отчество: ")
    tel = input("Введите телефон: ")
    data = open("phonebook.txt", 'a', encoding = "utf-8")
    data.writelines(f"фамилия: {lastname} имя: {name} отчество: {surname} телефон: {tel}\n")
    data.close()

def search():
    lookfor = input("Кого найти? ")
    with open("phonebook.txt", 'r', encoding = "utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)

def print_phonebook():
    with open("phonebook.txt", 'r', encoding = "utf-8") as data:
        for line in data:
            print(line)

def load():
    new_phonebook = input("Введите ссылку: ")
    with open(new_phonebook, 'r', encoding = "utf-8") as data:
        with open("phonebook.txt", 'a+', encoding = "utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)

print("""Введите: 1 - добавлние персоны
2 - поиск
3 - вывод полного справочника
4 - импорт в файл""")
ask = int(input())
if ask == 1:
    writing_person()
elif ask == 2:
    search()
elif ask == 3:
    print_phonebook()
elif ask == 4:
    load()
else:
    print("Нет такой команды!")
