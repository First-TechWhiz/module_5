class House:

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        floor = 0
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
           for floor in range(new_floor):
            floor += 1
            print(int(floor))

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return str(f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

print(h1)
print(h2)
print(len(h1))
print(len(h2))