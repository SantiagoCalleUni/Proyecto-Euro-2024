# Clase Matches que representa un partido de fútbol
class Matches:
    def __init__(self, home, away, date, stadium):
        self.home = home
        self.away = away
        self.date = date
        self.stadium = stadium
    
    def __str__(self):
        return f"{self.home.name} vs {self.away.name} en {self.stadium.name} el {self.date}"
    
    # Método para convertir el objeto a un diccionario
    def to_dict(self):
        return {
            'Equipo local': self.home.to_dict(),
            'Equipo visitante': self.away.to_dict(),
            'Fecha': self.stadium.date,
            'Estadio': self.stadium.to_dict()
        }
  