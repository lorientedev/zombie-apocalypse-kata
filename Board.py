class Board:

    size = 0
    board = [[]]
    charcters = {}

    def __init__(self, size):
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]

    def add(self, board_element, x, y):
        self.board[x][y] = board_element

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

    #Hay que definir que los zombies y supervivientes no puedan salir del mapa







