import os

clients_folder = './clients'

class Client:
    def __init__(self, name, age, children, **kwargs):
        self.name = name
        self.age = age
        self.children = children

        for arg in kwargs.items():
            print(arg)

def extract_client_info():
    for file in os.listdir(clients_folder):
        entire_path = os.path.join(clients_folder, file)

        with open(entire_path, 'r') as f:
            for line in f.readlines():
                print(line)

# client = Client('barbara', 22, 1, local = 'piscina', camas= 3)
# print(client.name)