from input import input_pupil, input_class1

def input_data():
    pupil = input_pupil()
    class1 = input_class1()
    
    with open('text1.txt', 'a', encoding='utf-8') as file:
        file.write(f'{pupil}, {class1}\n')
    print("Запись успешно сохранена")

def print_data():
    print('Вывод данных: ')
    with open('text1.txt', 'r', encoding='utf-8') as file:
        text1 = file.readlines()
        text2 = []
        j = 0
        for i in range(len(text1)):
            if text1[i] == '\n' or i == len(text1) - 1:
                text2.append(''.join(text1[j:i+1]))
                j = 1
        text1 = text2 
        print(''. join(text1))
    return text1

def delete_data():
    text1 = print_data()
    print("Какую запись по счету нужно удалить?")
    record_number = int(input('Введите номер записи: '))
    record_number -=1
    print(f'Удалить запись\n{text1[record_number - 1]}')
    text1 = text1[:record_number] + text1[record_number + 1:]
    with open('text1.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(text1))
    print('Изменения сохранены')

