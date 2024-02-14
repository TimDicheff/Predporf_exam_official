import csv
# Импортируем библиотеку csv
def create_password(Planet, Shipname):
    '''
    Функция, генерирующая пароль, удовлетворяющий условию
    Planet: аргумент, с помощью которого выполняются 1ое и 3ее условия создания пароля(передаем информацию о планете корабля)
    Shipname: аргумент, с помощью которого выполняется 2ое условие создание пароля(передаем информацию о названии корабля)
    '''
    first_part = (Planet[-3:]).upper()
    second_part = Shipname[1:3][::-1]
    third_part = (Planet[:3]).upper()
    password = f'{first_part}{second_part}{third_part}'
    return password

with open('space.txt', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='*')
    ships_list = list(reader)[1:]
# Открываем файл, создаем csv файл с исходными данными

    for ship in ships_list:
        password = create_password(ship[1], ship[0])
        ship.append(password)
# Для кадого корабля гененрируем и добавляем пароль

with open('space_uniq_password.csv', 'w', newline='', encoding='utf=8') as new_file:
    writer = csv.writer(new_file, delimiter='*')
    writer.writerow(['ShipName', 'planet', 'coord_place', 'direction', 'password'])
    writer.writerows(ships_list)
# Записываем новую таблицу данных с паролями в csv файл
