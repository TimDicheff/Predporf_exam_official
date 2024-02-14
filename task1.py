import csv

with open('space.txt', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='*')
    ships_list = list(reader)[1:]

    for ShipName, planet, coord_place, direction in ships_list:
        if int(coord_place[0]) + int(coord_place[-1]) == 0:
            if int(ShipName[-3]) > 5 and int(ShipName[-2]) > 3:
                coord_place = f'{int(ShipName[-3]) + int(direction[0:(len(direction) // 2)])} {int(ShipName[-2]) + len(planet) + int()}'
