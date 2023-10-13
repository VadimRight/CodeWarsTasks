class Person:
    name = None
    age = None

    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hi! My name is {self.name} and I am {self.age} years old'

    def __repr__(self):
        return self.__str__()


class People:
    def __init__(self, people=None):
        if people is None:
            people = []
        self.people = people

    def add_Person(self, person):
        if isinstance(person, Person):
            self.people.append(person)
        else:
            return 'Invalid person object'

    def __str__(self):
        return f'Greetings! There are {len(self.people)} people in the list.\n' + ', '.join(str(person) for person in self.people)

    def __repr__(self):
        return self.__str__()


girl = Person('Maria', 15)
boy = Person()
boy.name = 'Sasha'
boy.age = 19
print(girl)
print(boy)
people = People()
people.add_Person(girl)
people.add_Person(boy)
print(people)
