from DataManager import DataManager

class Menu(DataManager):
    def __init__(self):
        super().__init__()
        self.load_data_api()
        
    def display_menu(self):
        while True:
            print("\nMenú Principal")
            print("1. Comprar Tickets")
            print("2. Comprar en Restaurante")
            print("3. Marcar Asistencia")
            print("4. Revisar Información de Partidos")
            print("5. Salir")
            
            choice = input("Seleccione una opción: ")
            
            if choice == '1':
                self.buy_ticket()
            elif choice == '2':
                self.buy_in_restaurant()
            elif choice == '3':
                self.mark_attendance()
            elif choice == '4':
                self.view_match_info()
            elif choice == '5':
                break
            else:
                print("Opción no válida, intente de nuevo.")
    
    def buy_ticket(self):
        print("\nComprar Ticket")
        client_name = input("Nombre del cliente: ")
        id_number = int(input("Número de identificación: "))
        age = int(input("Edad: "))
        match_id = int(input("ID del partido: "))
        ticket_type = input("Tipo de ticket (General/VIP): ")
        
        self.data_manager.sell_ticket(client_name, id_number, age, match_id, ticket_type)
    
    def buy_in_restaurant(self):
        print("\nComprar en Restaurante")
        client_name = input("Nombre del cliente: ")
        id_number = int(input("Número de identificación: "))
        age = int(input("Edad: "))
        match_id = int(input("ID del partido: "))
        match = self.data_manager.search_match_id(match_id)
        
        if not match:
            print("Partido no encontrado")
            return
        
        stadium = match.stadium
        print(f"Estadio: {stadium.name}")
        print("Restaurantes disponibles:")
        for restaurant in stadium.restaurants:
            print(f"ID: {restaurant.id}, Nombre: {restaurant.name}")
        
        restaurant_id = int(input("Seleccione el ID del restaurante: "))
        selected_restaurant = None
        
        for restaurant in stadium.restaurants:
            if restaurant.id == restaurant_id:
                selected_restaurant = restaurant
                break
        
        if not selected_restaurant:
            print("Restaurante no encontrado")
            return
        
        ordered_products = []
        while True:
            product_name = input("Nombre del producto: ")
            quantity = int(input("Cantidad: "))
            ordered_products.append({"stadium_id": stadium.id, "product_name": product_name, "quantity": quantity})
            
            more = input("¿Desea agregar más productos? (s/n): ")
            if more.lower() != 's':
                break
        
        self.data_manager.process_order(client_name, id_number, age, ordered_products)
    
    def mark_attendance(self):
        sale_id = int(input("ID de la venta: "))
        self.data_manager.mark_attendance(sale_id)
    
    def view_match_info(self):
        print("\nInformación de los partidos:")
        self.data_manager.show_matches_info()

menu = Menu()
menu.display_menu()
