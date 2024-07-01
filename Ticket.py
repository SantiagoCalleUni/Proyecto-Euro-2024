from Client import Client

# Clase Ticket que representa un ticket de entrada a un partido
class Ticket(Client):
    def __init__(self, client_name, id_number, age, ticket_type, price, discount=0):
        super().__init__(client_name, id_number, age)  # Llamada al constructor de la clase padre (Client)
        self.ticket_type = ticket_type
        self.price = price
        self.discount = discount
        self.seat = None
    
    # Método para calcular el total del ticket incluyendo el descuento e impuestos  
    def calculate_total(self):
        subtotal = self.price - self.discount
        tax = subtotal * 0.16
        total = subtotal + tax
        return subtotal, tax, total

    def __str__(self):
        return f'Ticket Type: {self.ticket_type}, Price: {self.price}, Discount: {self.discount}, Seat: {self.seat}'

    # Método para confirmar la venta del ticket
    def confirm_sale(self, client, match, subtotal, tax, total):
        print(f"Venta confirmada para {client.name}")
        print(f"Partido: {match}")
        print(f"Asiento: {self.seat}")
        print(f"Subtotal: {subtotal}")
        print(f"IVA: {tax}")
        print(f"Total: {total}")
