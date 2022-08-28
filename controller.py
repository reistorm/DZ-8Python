from logger import input_data, delete_data, print_data

def button():
    print('Доступны 3 функции:\n'
          '1. Записать данные\n'
          '2. Удалить данные\n'
          '3. Вывести данные\n')
    operation = int(input('Введите номер операции: '))

    while operation > 3 or operation < 1:
        print('Неправильно введена команда!')
        operation = int(input('Введите номер операции: '))

    if operation == 1:
        input_data()
    if operation == 2:
        delete_data()
    if operation == 3:
        print_data()
    