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