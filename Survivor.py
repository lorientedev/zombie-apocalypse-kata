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
        success = False
        if position == "LeftHand":
            if (self.leftHandItem == None):
                self.leftHandItem = item
                success = True
            elif len(self.backpackItems) < 3:
                self.backpackItems.append(self.leftHandItem)
                self.leftHandItem = item
                success = True
        elif position == "RightHand":
            if (self.rightHandItem == None):
                self.rightHandItem = item
                success = True
            elif len(self.backpackItems) < 3:
                self.backpackItems.append(self.rightHandItem)
                self.rightHandItem = item
                success = True
        elif position == "Backpack":
            if len(self.backpackItems) < 3:
                self.backpackItems.append(item)
                success = True

        yield success

    def moveItem(self, item_name, new_position):
        item_found = None
        if item_name == self.leftHandItem.name:
            item_found = self.leftHandItem
        elif item_name == self.rightHandItem.name:
            item_found = self.rightHandItem
        for item in self.backpackItems:
            if item_name == item.name:
                item_found = item
        if item_found == None:
            pass
        if new_position == "LeftHand":
            if (self.leftHandItem == None):
                self.leftHandItem = item_found
        elif new_position == "RightHand":
            if (self.rightHandItem == None):
                self.rightHandItem = item_found
        elif new_position == "Backpack":
            if len(self.backpackItems) < 3:
                self.backpackItems.append(item_found)
        elif new_position == "Floor":

        






        