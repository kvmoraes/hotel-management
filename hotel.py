class Client:
    def __init__(self, name, age, children, **kwargs):
        self.name = name
        self.age = age
        self.children = children

        for arg in kwargs:
            print(arg)