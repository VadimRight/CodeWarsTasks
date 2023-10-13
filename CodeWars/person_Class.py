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


girl = Person('Maria', 15)
boy = Person()
boy.name = 'Sahsa'
boy.age = 19
print(girl)
print(boy)