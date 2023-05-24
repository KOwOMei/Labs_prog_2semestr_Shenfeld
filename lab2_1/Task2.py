# Напишите программу, которая определяет, какой тип места в плацкартном вагоне 
# (верхнее или нижнее, в купе или боковое) по заданному номеру места.

seat = int(input('Tell me your seat number on the train: '))

if seat in (1, 54):
    if seat in range(37, 54):
        print('Your seat is on the side.')
    else:
        print('Your seat is in the compartment.')

    if seat % 2 == 0:
        print("Your seat is downstairs.")
    else:
        print("Your seat is upstairs.")
else:
    print("This seat doesn't exist.")