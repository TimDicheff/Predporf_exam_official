import csv
# Импортируем библиотеку csv
with open('space.txt', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='*')
    ships_list = list(reader)
# Открываем файл, создаем csv файл с исходными данными

    name = input()
    while name != 'stop':
        for ship in ships_list:
            if ship[0] == name:
                print(f'Корабль {ship[0]} был отправлен с планеты: {ship[1]} и его направление движения было: {ship[-1]}')
                break
        else:
            print('error.. er.. ror..')
        name = input()
# Создаем цикл, удовлетворяющий условию, работающтий до команды 'stop'

