
import sys

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

            print(survivals, zombies, items, map_size, instructions)
            count = count + 1
            continue

        if parsing_survival_item and parsed_assigned_items < items_survival:
            print("parsed assigned items", parsed_assigned_items, "items survival", items_survival, "item", data)
            #print("Parse item ", data)
            parsed_assigned_items +=1
            continue
        elif parsing_survival_item and parsed_assigned_items == items_survival :
            parsing_survival_item = False
            parsed_assigned_items = 0
            items_survival = 0

        if parsed_survivals < survivals:
            
            if not parsing_survival_item:
                print("Parsed survivals ", data)
                parsed_survivals += 1 
                items_survival = int(data.split(" ")[2])
                if items_survival > 0:
                    parsing_survival_item = True
                continue
        
        if parsed_zombies < zombies:
            print("Parsed zombies", data)
            parsed_zombies += 1
            continue
        
        if parsed_items < items:
            print("Parsed items", data)
            parsed_items += 1
            continue
        if data == '':
            break

