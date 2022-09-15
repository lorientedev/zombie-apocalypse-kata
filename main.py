
import sys

import Board
import Survivor
import Item
import Zombie

input_file_name = sys.argv[1]

survivals = 0
parsed_survivals = 0
parsed_assigned_items = 0
parsing_survival_item = False
zombies = 0
parsed_zombies = 0
items = 0 
parsed_items = 0
map_size = 0
items_survival = 0
instructions = 0
parsed_instructions = 0
count = 0
board = None
survival = None

def create_board(size):
    return Board.Board(size)

def create_survival(data):
    data = data.split(" ")
    life = int(data[0])
    experience = int(data[1])
    x = int(data[3])
    y = int(data[4])
    name = data[5]
    return Survivor.Survivor(name, life, experience, x, y)

def create_zombie(data):
    data = data.split(" ")
    name = data[0]
    x = int(data[1])
    y = int(data[2])
    return Zombie.Zombie(name, x, y)

def create_item_survivor(data):
    data = data.split(" ")
    name = data[0]
    return Item.Item(name, 0,0)

def create_item(data):
    data = data.split(" ")
    name = data[0]
    x = int(data[1])
    y = int(data[2])
    return Item.Item(name, x, y)

with open(input_file_name) as f:
    while True:
        data = f.readline()
        if count == 0:
            survivals, zombies, items, map_size, instructions = data.split(" ")
            survivals = int(survivals)
            zombies = int(zombies)
            items = int(items)
            map_size = int(map_size)
            instructions = int(instructions)

            #print(survivals, zombies, items, map_size, instructions)
            board = create_board(map_size)
            count = count + 1
            continue

        if parsing_survival_item and parsed_assigned_items < items_survival:
            #print("parsed assigned items", parsed_assigned_items, "items survival", items_survival, "item", data)
            item = create_item_survivor(data)
            position = data.split(" ")[1]

            survival.addItem(position, item)
            parsed_assigned_items +=1
            continue
        elif parsing_survival_item and parsed_assigned_items == items_survival :
            parsing_survival_item = False
            parsed_assigned_items = 0
            items_survival = 0
            board.add(survival, survival.x, survival.y)

        if parsed_survivals < survivals:
            
            if not parsing_survival_item:
                #print("Parsed survivals ", data)
                
                survival = create_survival(data)
                parsed_survivals += 1 
                items_survival = int(data.split(" ")[2])
                if items_survival > 0:
                    parsing_survival_item = True
                continue
        
        if parsed_zombies < zombies:
            #print("Parsed zombies", data)
            zombie = create_zombie(data)
            board.add(zombie, zombie.x, zombie.y)
            parsed_zombies += 1
            continue
        
        if parsed_items < items:
            #print("Parsed items", data)
            item = create_item(data)
            board.add(item, item.x, item.y)
            parsed_items += 1
            continue
        if data == '':
            break
