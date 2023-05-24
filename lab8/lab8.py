from PIL import Image, ImageDraw, ImageFont
import os
import random

holiday_cards = {
    "Happy 8Day": "birthday_card.png",
    "New Year": "new_year_card.png",
    "Valentine's Day": "valentine_card.png"
}

holiday_name = input("Print the name of the holiday: ")
if holiday_name in holiday_cards:
    card_file = holiday_cards[holiday_name]
    card_img = Image.open(card_file)
    card_img.show()

    # Запрос координаты начала обрезки
    left = int(input("Введите X-координату левого верхнего угла: "))
    top = int(input("Введите Y-координату левого верхнего угла: "))

    # Запрос размера кадра
    width = int(input("Введите ширину кадра: "))
    height = int(input("Введите высоту кадра: "))

    # Вырезаем кадр
    cropped_card = card_img.crop((left, top, left + width, top + height))

    # Сохраняем изображение в текущую директорию с новым именем
    new_filename = "cropped_" + card_file
    cropped_card.save(new_filename)

    # Запрос имени для поздравления
    name = input("Кого мы будем поздравлять? ")

    # Создание объекта ImageDraw для написания текста 
    draw = ImageDraw.Draw(cropped_card)

    # Настройка параметров шрифта и цвета
    font_size = 30
    font = ImageFont.truetype("arial.ttf", font_size)
    text_color = (255, 0, 0)  # красный

    # Рассчет координат, по которым расположим текст "Имя, поздравляю!"
    text_width, text_height = draw.textsize(name, font=font)
    x = (cropped_card.width - text_width) // 2  # по центру
    y = cropped_card.height * 0.1  # вверху

    # Добаление текста на полученное изображение
    draw.text((x, y), f"{name}, поздравляю!", fill=text_color, font=font)

    # Сохраняем новое изображение
    new_filename = "greeting_" + card_file
    cropped_card.save(new_filename)
else:
    print("Праздник не найден :(")


