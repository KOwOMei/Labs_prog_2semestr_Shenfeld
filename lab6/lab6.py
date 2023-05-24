# Создаем словарь с перечнем стран и их столиц
countries = {"Russia": "Moscow",
             "USA": "Washington, D.C.",
             "France": "Paris",
             "Germany": "Berlin",
             "China": "Beijing"}

# a) Выводим на экран все пары ключ-значение
for country, capital in countries.items():
    print(country, "-", capital)

# b) Выводим на экран столицу для определенной страны
try:
    capital = input("\nGive me a name of Country, and I'll give you it's Capital: ")
    print(f"The capital of {capital} is {countries[capital.capitalize()]}\n")
except:
    print("Ops, I don't know Capital of this Country :(\n")

# c) Сортируем и выводим на экран содержимое словаря в алфавитном порядке названий стран
sorted_countries = sorted(countries)
for country in sorted_countries:
    print(country, "-", countries[country])

# Создаем словарь со значениями очков для каждой буквы
scores = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1,
          'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1,
          'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3,
          'Э': 8, 'Ю': 8, 'Я': 3}

# Запрашиваем у пользователя слово
word = input("\nPrint a word in Russian: ")

# Вычисляем стоимость слова
score = 0
for letter in word.upper():
    score += scores.get(letter, 0)
    
# Выводим стоимость слова на экран
print(f"The word '{word}' costs {score} points.")
