from PIL import Image, ImageDraw, ImageFont
import os
import random

holiday_cards = {
    "Happy Birthday": "birthday_card.png",
    "New Year": "new_year_card.png",
    "Valentine's Day": "valentine_card.png"
}

holiday_name = input("Enter the name of the holiday: ")
if holiday_name in holiday_cards:
    card_file = holiday_cards[holiday_name]
    card_img = Image.open(card_file)
    card_img.show()

    # Request for cropping coordinates
    left = int(input("Enter the X-coordinate of the top-left corner: "))
    top = int(input("Enter the Y-coordinate of the top-left corner: "))

    # Request for cropped frame size
    width = int(input("Enter the width of the frame: "))
    height = int(input("Enter the height of the frame: "))

    # Crop the image
    cropped_card = card_img.crop((left, top, left + width, top + height))

    # Save the new image with a different name 
    cropped_card.save(f"cropped_{card_file}")

    # Request for the name to congratulate
    name = input("Who are we congratulating? ")

    # Create an ImageDraw object to write text
    draw = ImageDraw.Draw(cropped_card)

    # Set font and color options
    font_size = 30
    font = ImageFont.truetype("arial.ttf", font_size)
    text_color = (255, 0, 0)  # red

    # Calculate the coordinates for the "Name, congratulations!" text
    text_width, text_height = draw.textsize(name, font=font)
    x = 0  # centered
    y = cropped_card.height * 0.1  # top

    # Add text to the cropped image
    draw.text((x, y), f"{name}, congrats! {holiday_name}!", fill=text_color, font=font)

    # Save the new image
    cropped_card.save(f"greeting_{card_file}")
else:
    print("Holiday not found :(")
