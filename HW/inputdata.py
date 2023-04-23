from data_create import *


def input_data():
    name = name_data()
    lastname = lastname_data()
    phone = phone_data()

    with open("d:/Обучение/Програмирование/Python/Lesson_8/HW/phonebook.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{lastname}\t{name}\t{phone}")


def print_data():
    with open("d:/Обучение/Програмирование/Python/Lesson_8/HW/phonebook.txt", 'r', encoding="utf-8") as data:
        data_first = data.read()
        print(data_first)


def search():
    lookfor = input("Кого найти? ")
    bool_1 = False
    with open("d:/Обучение/Програмирование/Python/Lesson_8/HW/phonebook.txt", 'r', encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)
                bool_1 = True
        if bool_1 == False:
            print("Нет такого контакта")

def delite_contact():
    line_str = input("Введите контакт, который нужно удалить: ")
    with open("d:/Обучение/Програмирование/Python/Lesson_8/HW/phonebook.txt", 'r', encoding="utf-8") as data:
        lines = data.readlines()
        with open("d:/Обучение/Програмирование/Python/Lesson_8/HW/phonebook.txt", 'w', encoding="utf-8") as data_1:
            for line in lines:
                if line_str not in line:
                    data_1.write(line)

def change_contact():
    line_str = input("Введите контакт, который хотите изменить: ")
    with open("d:/Обучение/Програмирование/Python/Lesson_8/HW/phonebook.txt", 'r', encoding="utf-8") as data:
        lines = data.readlines()
        with open("d:/Обучение/Програмирование/Python/Lesson_8/HW/phonebook.txt", 'w', encoding="utf-8") as data_1:
            for line in lines:
                if line_str not in line:
                    data_1.write(line)
                else:
                    name = input("Введите новое имя: ")
                    lastname = input("Введите новую фамилию: ")
                    phone = input("Введите новый телефон: ")
                    data_1.write(f"{lastname}\t{name}\t{phone}")
