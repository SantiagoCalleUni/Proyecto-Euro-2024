from Restaurant import Restaurant

class Product(Restaurant):
    def __init__(self, id, name, city, capacity, classification, product_name, type_detail, price, quantity, alcoholic=False):
        super().__init__(id, name, city, capacity, classification)
        self.product_name = product_name
        self.type_detail = type_detail
        self.price = price + (price * 0.16)  # Agregar IVA del 16%
        self.quantity = quantity
        self.alcoholic = alcoholic

    def __str__(self):
        return f"{self.product_name}, {self.classification}, {self.type_detail}, ${self.price:.2f}, Cantidad: {self.quantity}, Alcohólica: {self.alcoholic}"

    def to_dict(self):
        return {
            'name': self.product_name,
            'classification': self.classification,
            'type_detail': self.type_detail,
            'price': self.price,
            'quantity': self.quantity,
            'alcoholic': self.alcoholic
        }
