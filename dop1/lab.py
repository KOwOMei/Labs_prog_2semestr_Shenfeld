import re
from collections import UserDict

def find_syns(word, dict):  # Объявляем функцию по поиску нужных синонимов в нашей базе данных.
    """Функция ищет синонимы к выбранному слову. Формат данных: word - Слово, к которому мы и будем искать синонимы; dict - наш словарь формата 'Слово - Синоним';
    На выходе получаем список новых синонимов к слову, если они были введены пользователем, а также логический выход по нахождению слова."""
    new_syn_list = []  # Задаем пустой массив, в будущем будет использоваться для хранения новых синонимов.
    find = False
    for i in range(len(dict)):  # Ищем все возможные синонимы к слову
        if word in dict[i]:
            find = True
            print('The existing synonyms for this word are:', re.sub(f"{word} - ", '', dict[i]))

    while find:  # В случае нахождения синонимов к слову - предлагаем ввести свои.
        ans = str(input(f"Do you want to add more synonyms to {word}?: "))
        if ans.capitalize() == "Да" or ans.capitalize() == "Yes":
            new_syn = str(input('Write the synonym: '))
            new_syn_list.append(new_syn)
            print("Added a new synonym to list.")
        elif ans.capitalize() == "Нет" or ans.capitalize() == "No":
            print("So be it...")
            break
    return new_syn_list, find

with open(r"synonyms.txt", "r", encoding="utf-8") as file: # Открываем наш словарь через кодировку utf-8.
    dict_base = list(file)

idk = "; " # Объявляем переменную, отвечающую за будущую запись синонимов.
word_base = str(input('Write the word you want to see synonyms for: ')) # Запрашиваем слово, к которому и будем искать синонимы.
word_base = word_base.capitalize()
syn_list, ex = find_syns(word_base, dict_base) # Обращаемся к функции, передавая ему слово и словарь. Получаем на выходе список новых синонимов и результат нахождения синонимов.

if ex != True: # Проверяем нахождение синонимов к слову.
    print('This word doesnt exist in the database, sorry :(')

if syn_list != []: # Проверяем заполненность массива с новыми синонимами.
    with open(r"synonyms.txt", "a", encoding="utf-8") as file:
        file.writelines(f"\n{word_base} - {idk.join(str(x) for x in syn_list)}")