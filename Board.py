from shutil import move


class Board:

    size = 0
    board = [[]]
<<<<<<< HEAD
    characters = {}
=======
    charcters = {}
>>>>>>> eb44e3e5c7fc82d7802f814b111fffea77a6e273

    def __init__(self, size):
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]

    def add(self, board_element, x, y):
        self.board[x][y] = board_element
        self.characters[board_element.name] = {"x":x, "y":y, "element": board_element}

<<<<<<< HEAD
    def executeInstruction(self, instruction):
        if instruction.type == "M":
            character_position = self.characters[instruction.character_name]
            moveCharacter(character_position, instruction.direction)
        elif instruction.type == "P":
            character_position = self.characters[instruction.character_name]
            item_position = self.characters[instruction.item_name]
            item_added = character_position.element.addItem(self, instruction.spot, item_position.element)
            if item_added == True:
                self.board[item_position.x][item_position.y] = 0
        elif instruction.type == "R":
            

        elif instruction.type == "A":


    def moveCharacter(self, character_position, movement):
        self.board[character_position.x][character_position.y] = 0
        if movement == "Up":
            self.add(self, character_position.element, character_position.x, character_position.y+1)
        elif movement == "Down":
            self.add(self, character_position.element, character_position.x, character_position.y-1)
        elif movement == "Right":
            self.add(self, character_position.element, character_position.x+1, character_position.y)
        elif movement == "Left":
            self.add(self, character_position.element, character_position.x-1, character_position.y)
       
=======
    #def executeInstruction(self, instruction):
    #    if instruction.type == "M":
    #        
    #    elif instruction.type == "P":
    #
    #    elif instruction.type == "R":
    #
    #    elif instruction.type == "A":
    #

    #def findCharacter(self, type):
>>>>>>> eb44e3e5c7fc82d7802f814b111fffea77a6e273

    #Hay que definir que los zombies y supervivientes no puedan salir del mapa







