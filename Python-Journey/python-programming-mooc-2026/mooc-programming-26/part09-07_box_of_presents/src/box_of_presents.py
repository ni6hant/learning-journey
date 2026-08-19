# WRITE YOUR SOLUTION HERE:
class Present:
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
    
    def __init__(self, name:str, weight: int):
        self.name = name
        self.weight = weight

class Box:
    def __init__(self):
        self.total_weight_of_box = 0
        self.contents = []
        pass

    def add_present(self, present: Present):
        self.contents.append(present)
        self.total_weight_of_box += present.weight

    def total_weight(self):
        return self.total_weight_of_box