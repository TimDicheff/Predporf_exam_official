import csv

def create_hash(ShipName, planet):
    hash = {planet: ShipName}
    return hash

with open('space.txt', encoding='utf-8') as file:
     reader = csv.reader(file, delimiter='*')
     ships_list = list(reader)

     for ship in range(len(ships_list) - 89):
         ships_list.append(create_hash(ship[0], ship[1]))
         print(ships_list[ship])