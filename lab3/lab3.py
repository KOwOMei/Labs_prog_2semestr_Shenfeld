from random import randint


#С клавиатуры вводятся поочередно слова, пока пользователь не введет слово «stop»
#Напишите программу, которая соединяет эти слова в одну длинную строку, разделяя слова пробелами. 
#Используйте операторы цикла.
def num2():
    word = ''
    line = ''
    while word != 'stop':
        word = str(input('Write a word: '))

        if word != 'stop':
            line += word + ', '
        else:
            line = line[:len(line)-2] + "."
    print(line)

#Напишите программу, которая позволяет пользователям вводить какие-либо слова и проверяет, 
#можно считать это слово редким или нет. (редкие слова содержат букву "ф")
def num3():
    while (word := str(input('Write a word: '))) != 'stop':
        if "ф" in word.lower():
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово...')

# игра-математика. 
# Пользователь может бесконечно решать примеры, пока не совершит 3 ошибки или пока не напишет «stop»
def num4():
    mis = 0
    while mis != 3:
        a = randint(1, 10)
        b = randint(1, 10)
        res = input(f"{a} + {b} = ")
        if res == 'stop':
            break
        while not res.isdigit():
            res = input('Incorrect input. Try again: ')

        res = int(res)
        if a+b == res:
            print('Correct answer!')
        elif a+b != res:
            print('Oops. You are wrong!')
            mis += 1


print('Задание 1 и 2')
num2()
print('Задание 3')
num3()
print('Задание 4')
num4()