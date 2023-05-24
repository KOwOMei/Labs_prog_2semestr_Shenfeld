import os
from PIL import Image, ImageFilter

folder_path = input("Введите путь к папке: ")

files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg','.jpeg','.png'))]

if not os.path.exists('output'):
    os.makedirs('output')

for file in files:
    original_im = Image.open(os.path.join(folder_path, file))
    filtered_im = original_im.filter(ImageFilter.MinFilter)
    filtered_im.save(os.path.join('output', file))

with open("data.csv", encoding="utf-8") as file:
    # Пропускаем заголовок
    next(file)

    total = 0
    purchases = []

    for line in file:
        # Разделяем строку по запятой
        product, quantity, price = line.strip().split(",")

        # Преобразуем количество и цену в числа
        quantity = int(quantity)
        price = int(price)

        # Добавляем информацию о покупке в список
        purchases.append(f"{product} - {quantity} шт. за {price} руб.")

        # Подсчитываем общую стоимость покупок
        total += quantity * price

# Выводим результаты
print("Нужно купить:")
print("\n".join(purchases))
print(f"Итоговая сумма: {total} руб.")
