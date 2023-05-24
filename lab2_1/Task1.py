# При регистрации на сайтах требуется вводить пароль дважды. 
# Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля. 
# Напишите программу, которая сравнивает пароль и его подтверждение. 
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

password = input('Write your password: ')

numbers = False
capital = False
lowercase = False
special = False

for char in password:
    if char.isnumeric():
        numbers = True
    elif char.islower():
        lowercase = True
    elif char.isupper():
        capital = True
    elif char in "!@*&$.":
        special = True

if len(password) > 7 and numbers and capital and lowercase and special:
    print('Your password is strong!')
    confirmation = input('Confirm your password: ')
    if password == confirmation:
        print('Successful!')
    else:
        print("how can you mess this up? it's right in front of you...")
else:
    print ('Password is weak, you should add: ')
    if len(password) < 8:
        print('more characters')
    if numbers is False:
        print('numbers')
    if capital is False:
        print('uppercase letters')
    if lowercase is False:
        print('lowercase letters')
    if special is False:
        print('special symbols')