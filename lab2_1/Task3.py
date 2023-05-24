# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
# Напишите функцию, которая определяет, является ли год с данным номером високосным. 
# Если год является високосным, то выведите «Год ... - високосный», 
# где вместо многоточия выведите год, иначе выведите «Это год не високосный».

year = int(input('Tell me the year: '))

if (year % 4) == 0:
    if (year % 100) == 0 and (year % 400) == 0:
        print('This is a високосный год')
    elif (year % 100) == 0 and (year % 400) != 0:
        print(f'{year} is not a високосный год')
    else:
        print(f'{year} is a високосный год')
else:
    print(f'{year} is not a високосный год')
    