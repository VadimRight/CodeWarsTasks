class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs


def sort_animals(input):
    sorted(input, key=lambda Animal: (Animal.number_of_legs, Animal.name))