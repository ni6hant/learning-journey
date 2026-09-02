# Write your solution here:
class Item:
    def __init__(self, item_name:str, item_weight:int):
        self.item_name = item_name
        self.item_weight = item_weight

    def __str__(self):
        return f"{self.item_name} ({self.item_weight} kg)"

    @property
    def item_name(self):
        return self.__item_name

    @property
    def item_weight(self):
        return self.__item_weight

    @item_name.setter
    def item_name(self,item_name):
        if len(item_name) == 0:
            raise ValueError("Name of book can't be empty")
        self.__item_name = item_name

    @item_weight.setter
    def item_weight(self,item_weight):
        self.__item_weight = item_weight

    def weight(self):
        return self.__item_weight

    def name(self):
        return self.item_name

class Suitcase:
    def __init__(self,max_weight:int):
        self.max_weight = max_weight
        self.items = []

    def __str__(self):
        if len(self.items) == 1:
            return f"{len(self.items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.items)} items ({self.weight()} kg)"

    @property
    def max_weight(self):
        return self.__max_weight

    @max_weight.setter
    def max_weight(self,max_weight):
        self.__max_weight = max_weight

    def add_item(self,item:Item):
        if self.add_item_check(item):
            self.items.append(item)

    def add_item_check(self,item:Item):
        return (self.weight() + item.weight())<(self.max_weight)

    def weight(self):
        weight = 0
        for item in self.items:
            weight += item.weight()
        return weight

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        if len(self.items) == 0:
            return None
        else:
            heaviest_item = self.items[0]
            for item in self.items:
                if heaviest_item.item_weight < item.weight():
                    heaviest_item = item
            return heaviest_item

class CargoHold:
    def __init__(self,max_weight):
        self.max_weight = max_weight
        self.suitcases = []

    def __str__(self):
        if len(self.suitcases) == 1:
            return f"{len(self.suitcases)} suitcase, space for {(self.max_weight - self.weight())} kg"
        else:
            return f"{len(self.suitcases)} suitcases, space for {(self.max_weight - self.weight())} kg"

    @property
    def max_weight(self):
        return self.__max_weight

    @max_weight.setter
    def max_weight(self,max_weight):
        self.__max_weight = max_weight

    def add_suitcase(self,suitcase:Suitcase):
        if self.add_suitcase_check(suitcase):
            self.suitcases.append(suitcase)

    def add_suitcase_check(self,suitcase:Suitcase):
        return (self.weight() + suitcase.weight())<(self.max_weight)

    def weight(self):
        weight = 0
        for suitcase in self.suitcases:
            weight += suitcase.weight()
        return weight

    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(item)