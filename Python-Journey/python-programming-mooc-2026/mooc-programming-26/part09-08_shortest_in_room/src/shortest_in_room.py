# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.list_of_persons = []
        self.count_of_persons = 0
        self.combined_height = 0
        self.shortest_in_room = None

    def add(self,person:Person):
        self.list_of_persons.append(person)
        self.count_of_persons += 1
        self.combined_height += person.height
        if self.shortest_in_room is not None:
            if person.height<self.shortest_in_room.height:
                self.shortest_in_room = person
        else:
            self.shortest_in_room = person

    def is_empty(self):
        return len(self.list_of_persons)==0

    def print_contents(self):
        print(f"There are {self.count_of_persons} persons in the room, and their combined height {self.combined_height} cm")
        for person in self.list_of_persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.shortest_in_room is None:
            return None
        return self.shortest_in_room

    def remove_shortest(self):
        if len(self.list_of_persons) == 0:
            return None

        #Find the smallest Person    
        smallest_person = self.list_of_persons[0]
        for person in self.list_of_persons:
            if person.height<smallest_person.height:
                smallest_person = person

        #Index of the smallest person
        smallest_index = self.list_of_persons.index(smallest_person)
        self.combined_height -= smallest_person.height
        self.count_of_persons -= 1
        return self.list_of_persons.pop(smallest_index)


if __name__ == "__main__":
    room = Room()
    try:
        val = room.remove_shortest()
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(val is None, f'Method remove_shortest should return a value None, ' + 
            f'when the room is empty, now it returns a value {val}, which is of type {taip}.')
    except Exception as e:
        self.fail('Method call remove_shortest threw an error\n{e}' + 
            'when the room is empty.')