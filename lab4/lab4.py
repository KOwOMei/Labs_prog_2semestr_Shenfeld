# Напишите функцию, которая проверяет, делится ли введенное число на 3, или нет.
def t1(number: int):
    return True if number % 3 == 0 else False

# Напишите функцию деления числа 100 на введенное пользователем число.
def t2(number):
    result = 0
    try:
        result = 100 / float(number)
        return result
    except ValueError:
        return 'Incorrect input: use numbers'
    except ZeroDivisionError:
        return 'Division by 0 is impossible'
    except Exception as e:
        return 'ERROR'

# Напишите функцию, которая возвращает True, если введенная пользователем дата является магической
# False в обратном случае. Магической считается дата, в которой произведение дня и месяца 
# равно двум последним цифрам года, например: 02.11.2022.
def t3(date: str):
    date = date.split('.')
    try:
        if int(date[0])*int(date[1]) == int(date[2][2:4]):
            return True
        else:
            return False
    except:
        return 'The correct date input format is dd.mm.yyyy'

#
def t4(ticket:str):
    x = 0
    y = 0
    length = len(ticket)
    if length % 2 == 0:
        for i in range(length):
            if (i) < (length/2):
                x += int(ticket[i])
            else:
                y += int(ticket[i])

        if x == y:
            return 'Это счастливый билет!'
        else:
            return 'Это не счастливый билет('
    else:
        return 'Такое число не подходит'
    



print('Кратность числа на 3')
print(t1(14))
print(t1(15))

print('\nДеление 100 на число')
print(t2(100))
print(t2(3))
print(t2(0))
print(t2('gg'))
print(t2('reg'))

print('\nIs this a magical date?')
print(t3('02.11.2022'))
print(t3('01.07.2021'))
print(t3('01.07.21'))

print('\nIs this a lucky ticket?')
print(t4('123456'))
print(t4('123321'))
print(t4('23456'))