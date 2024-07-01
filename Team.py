# Clase Team que representa a un equipo de fútbol
class Team:
    def __init__(self, id, code, name, group):
        self.id = id 
        self.code = code
        self.name = name
        self.group = group
        
    def __str__(self):
            return f'Name: {self.name}, Group: {self.group}'
    
    # Método para convertir el objeto a un diccionario
    def to_dict(self):
        return {
            'ID': self.id,
            'Code': self.code,
            'Name': self.name,
            'Group': self.group
        }
