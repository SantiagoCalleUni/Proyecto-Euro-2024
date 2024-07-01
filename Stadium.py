from itertools import permutations # Esta función genera todas las posibles permutaciones de una secuencia. Es útil para verificar un número es vampiro

# Clase Stadium que hereda de Restaurant
class Stadium:
    def __init__(self, id, name, city, capacity):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = []
        
    def __str__(self):
        return f'Stadium: {self.name}, City: {self.city}, Capacity: {self.capacity}'
    
    # Método para inicializar los asientos del estadio
    def initialize_seats(self, capacity):
        seats = {}
        for i in range(1, capacity + 1):
            seats[f'A{i}'] = True  # Asiento disponible
        return seats
    
    # Método para asignar un asiento disponible
    def assign_seat(self):
        for seat, available in self.available_seats.items():
            if available:
                self.available_seats[seat] = False
                return seat
        return None
    
    @staticmethod
    # Metodo para saber si una cedula es un numero vampiro
    def vampire_number(num):
        num_str = str(num)
        # Verificar longitud de numeros
        if len(num_str) % 2 != 0:
            return False
        
        # Calcular la mitad de la longitud. el numero se va a dividir en dos partes iguales 
        half_len = len(num_str) // 2
        # Generar todas las permutaciones posibles
        permuts = permutations(num_str)
        # Iteramos en todas las permutaciones
        for perm in permuts:
            # Los numeros de la primera parte y la segunda parte se convierten en numeros enteros
            x = int(''.join(perm[:half_len]))
            y = int(''.join(perm[half_len:]))
            # Verificamos si el producto de estos dos números es igual al número original. Si es así, retornamos True.
            if x * y == num:
                return True
        return False
    
    # Método para mostrar el mapa del estadio
    def show_map(self):
        print("Mapa del estadio:")
        for seat, available in self.available_seats.items():
            status = "Disponible" if available else "Ocupado"
            print(f"Asiento {seat}: {status}")

    # Método para asignar asiento
    def assign_seat(self):
        for i in range(self.capacity):
            seat = f"Seat-{i+1}"
            if not self.available_seats[seat]:
                return seat
        return None
    
    # Método para agregar productos del restaurante
    def add_product(self, product):
        self.restaurants.append(product)

    # Método para buscar productos por nombre, tipo o rango de precio
    def search_products(self, name=None, product_type=None, price_range=None):
        result = []
        for product in self.restaurants:
            if name and name.lower() in product['name'].lower():
                result.append(product)
            elif product_type and product['type'].lower() == product_type.lower():
                result.append(product)
            elif price_range and price_range[0] <= product['price'] <= price_range[1]:
                result.append(product)
        return result

    # Método para restar del inventario la cantidad de productos comprados
    def update_inventory(self, purchased_products):
        for purchased_product in purchased_products:
            for product in self.restaurants:
                if product['name'] == purchased_product['name']:
                    product['quantity'] -= 1
                    break


