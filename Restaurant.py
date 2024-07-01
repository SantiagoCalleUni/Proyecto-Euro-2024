from Stadium import Stadium

# Clase Restaurant que hereda de Stadium y Product
class Restaurant(Stadium):
    def __init__(self, id, name, city, capacity, classification):
        super().__init__(id, name, city, capacity)
        self.classification = classification
        self.products = []

    def __str__(self):
        return f"Restaurante: {self.name}, Clasificación: {self.classification}"

    def add_product(self, product):
        self.products.append(product)

    def search_products(self, name=None, product_type=None, price_range=None):
        result = []
        for product in self.products:
            if name and name.lower() in product.name.lower():
                result.append(product)
            elif product_type and product.classification.lower() == product_type.lower():
                result.append(product)
            elif price_range and price_range[0] <= product.price <= price_range[1]:
                result.append(product)
        return result

    def update_inventory(self, purchased_products):
        for purchased_product in purchased_products:
            for product in self.products:
                if product.name == purchased_product.name:
                    product.quantity -= 1
                    break
