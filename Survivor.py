class Survivor:
    name = ""
    life = 0
    experience = 0
    backpackItems = []
    leftHandItem = None
    rightHandItem = None
    #x=0
    #y=0

    def __init__(self, name, life, experience):

        self.name = name
        self.life = life
        self.experience = experience

    def addItem(self, position, item):
        if position == "LeftHand":
            if (self.leftHandItem == None):
                self.leftHandItem = item
            elif len(self.backpackItems) < 3:
                self.backpackItems.append(self.leftHandItem)
                self.leftHandItem = item
        elif position == "RightHand":
            if (self.rightHandItem == None):
                self.rightHandItem = item
            elif len(self.backpackItems) < 3:
                self.backpackItems.append(self.rightHandItem)
                self.rightHandItem = item
        elif position == "Backpack":
            if len(self.backpackItems) < 3:
                self.backpackItems.append(item)
            
        






        