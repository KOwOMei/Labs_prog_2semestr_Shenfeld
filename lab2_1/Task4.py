# Напишите программу, которая считывает названия двух основных цветов для смешивания. 
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», 
# то программа должна вывести сообщение об ошибке. 
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

first_colour = input('Write the first colour: ')
second_colour = input('Write the second colour: ')

colours = ('red, blue, yellow')

if first_colour.lower() in colours and second_colour.lower() in colours:
    if first_colour.lower() == second_colour.lower():
        print (first_colour)
    elif (first_colour.lower() == 'red' or second_colour.lower() == 'red') and (first_colour.lower() == 'blue' or second_colour.lower() == 'blue'):
        print ('The colour we get would be purple.')
    elif (first_colour.lower() == 'red' or second_colour.lower() == 'red') and (first_colour.lower() == 'yellow' or second_colour.lower() == 'yellow'):
        print ('The colour we get would be orange.')
    elif (first_colour.lower() == 'yellow' or second_colour.lower() == 'yellow') and (first_colour.lower() == 'blue' or second_colour.lower() == 'blue'):
        print ('The colour we get would be green.')
else:
    print('Sorry, we dont process this kind of colours ^^')