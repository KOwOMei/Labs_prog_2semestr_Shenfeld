import json

with open('products.json') as file:
    data = json.load(file)

for product in data['products']:
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"Weight: {product['weight']}")
    if product['available']:
        print("Is available!")
    else:
        print("Not available!")

ask = input("Want to add a new product?: ")
if ask.capitalize() in ("Yes","Y", "Да", "Д"):
    name = input("Print a name of the product: ")
    price = float(input("Product price: "))
    weight = int(input("Product weight: "))
    available = input("Are available? (y/n): ").lower()
    available = True if available == "y" else False
    new_product = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }

    # Добавляем новый продукт в список
    data['products'].append(new_product)

    # Обновляем файл
    with open('products.json', 'w') as file:
        json.dump(data, file)

# Открываем файл для чтения
with open('en-ru.txt', 'r') as f:
    # Создаем словарь
    dictionary = {}
    for line in f:
        # Разбиваем строку на английские и русские слова
        parts = line.strip().split(' - ')
        if len(parts) < 2: 
            # Если получено меньше двух элементов, то строка не является валидной и мы ее пропускаем
            continue
        eng_word, rus_words = parts[0], parts[1]
        if eng_word in dictionary:
            dictionary[eng_word].extend(rus_words.split(', '))
        else:
            dictionary[eng_word] = rus_words.split(', ')

# Сортируем элементы словаря по ключам
sorted_dict = dict(sorted(dictionary.items()))

# Открываем файл для записи
with open('ru-en.txt', 'w') as f:
    # Выводим отсортированные элементы словаря в файл ru-en.txt
    for eng_word, rus_words in sorted_dict.items():
        f.write('{} - {}\n'.format(', '.join(rus_words), eng_word))
