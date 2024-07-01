# Clase Client que representa a un cliente
class Client:
    def __init__(self, name, id_number, age):
        self.name = name
        self.id_number = id_number
        self.age = age

    def __str__(self):
        return f'Client: {self.name}, ID: {self.id_number}, Age: {self.age}'
    
