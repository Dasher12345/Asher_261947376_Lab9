class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class House:
    def __init__(self, address, num_rooms):
        self.address = address
        self.num_rooms = num_rooms
        self.residents = []

    def add_resident(self, person):
        self.residents.append(person)

    def remove_resident(self, person):
        if person in self.residents:
            self.residents.remove(person)
        else:
            print(person.name, "is not a resident of this house.")

    def print_residents(self):
        print("Residents of",self.address)
        for resident in self.residents:
            print("\t",resident.name, resident.age)




# create some Person objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Asher", 20)

# create a House object
my_house = House("123 Main St.", 3)

# add residents to the House
my_house.add_resident(person1)
my_house.add_resident(person2)

my_house.remove_resident(person2)
my_house.remove_resident(person3)
# print out the residents of the House
my_house.print_residents()
