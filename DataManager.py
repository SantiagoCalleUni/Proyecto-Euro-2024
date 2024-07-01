import requests
import json 
from Team import Team
from Stadium import Stadium
from Restaurant import Restaurant
from Product import Product
from Matches import Matches
from Client import Client
from Ticket import Ticket

# Clase "DataManager" con listas vacias para almacenar los equipos, estadios y partidos.
class DataManager(Stadium, Team, Client, Restaurant, Ticket):
    def __init__(self):
        super().__init__()
        self.teams = []
        self.stadiums = []
        self.matches = []
        self.sales = []
        
    # Metodo para cargar todas las APIs 
    def load_data_api(self):
        # Cargar equipos
        team_data = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json').json()
        for team in team_data:
            # Creando una instancia del la clase Team y agregando valores expecificos de la API
            new_team = Team(team['id'], team['code'], team['name'], team['group'])
            self.teams.append(new_team)
            
        # Cargar estadios
        team_stadium = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json').json()
        for stadium in team_stadium:
            # Creando una instancia del la clase Stadium y agregando valores expecificos de la API
            new_stadium = Stadium(stadium['id'], stadium['name'], stadium['city'], stadium['capacity'])
            # Añadir restaurante
            restaurant_data = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/restaurants.json').json()
            for restaurant in restaurant_data:
                new_restaurant = Restaurant(restaurant['id'], restaurant['name'], restaurant['classification'])
                for product in restaurant['products']:
                    new_product = Product(
                        product['id'],
                        product['name'],
                        product['classification'],
                        product.get('type_detail', ''),
                        product['price'],
                        product['quantity'],
                        product.get('alcoholic', False)
                    )
                    new_restaurant.add_product(new_product)
                new_stadium.add_restaurant(new_restaurant)
            self.stadiums.append(new_stadium)
            
        # Cargar partidos
        match_data = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json').json()
        for match in match_data:
            local_team = self.search_team_id(match['home_team'])
            visitant_team = self.search_team_id(match['away_team'])
            date = match['date']
            stadium = self.search_stadium_id(match['stadium_id'])
            # Creando una instancia del la clase Matches y agregando valores expecificos de la API
            new_match = Matches(local_team, visitant_team, date, stadium)
            self.matches.append(new_match)
            
    # Guardando los datos de las APIs en formato JSON
    def save_data_file(self, Team_File, Stadium_File, Matches_File):
        with open(Team_File.json, 'w', encoding='utf-8') as t:
            # Convertir cada objeto Team en la lista self.equipos a un diccionario 
            json.dump([team.to_dict() for team in self.teams], t, ensure_ascii=False, indent=4)
            
        with open(Stadium_File.json, 'w', encoding='utf-8') as s:
            # Convertir cada objeto Team en la lista self.equipos a un diccionario
            json.dump([stadium.to_dict() for stadium in self.stadiums], s, ensure_ascii=False, indent=4)
            
        with open(Matches_File.json, 'w', encoding='utf-8') as m:
            # Convertir cada objeto Team en la lista self.equipos a un diccionario
            json.dump([match.to_dict() for match in self.matches], m, ensure_ascii=False, indent=4) 
    
    # Metodo para buscar partidos por pais 
    def search_matches_countrys(self, country):
        return [match for match in self.matches if match.home.name.lower() == country.lower() or match.away.name.lwer() == country.lower()]
    
    # Metodo para buscar partidos por estadios 
    def search_matches_stadium(self, stadium_name):
        return [match for match in self.matches if match.stadium.name == stadium_name]
    
    # Metodo para buscar partidos por partidos
    def search_matches_date(self, date):
        return [match for match in self.matches if match.date.startswith(date)]
    
    # Metodo para buscar partido por id 
    def search_match_id(self, match_id):
        for match in self.matches:
            if match.id == match_id:
                return match
        return None
    
    # Metodo para buscando equipo por id
    def search_team_id(self, id):
        for team in self.teams:
            if team.id == id:
                return team
        return None

    # Metodo para buscando estadio por id
    def search_stadium_id(self, id):
        for stadium in self.stadiums:
            if stadium.id == id:
                return stadium
        return None
    
    # Método para mostrar información de los partidos
    def show_matches_info(self):
        for match in self.matches:
            print(match)

    # Método para mostrar el mapa del estadio
    def show_stadium_map(self, match_id):
        match = self.search_match_id(match_id)
        if not match:
            print("Partido no encontrado")
            return
        match.stadium.show_map()
    
    # Metodo para la venta de tickets y disponibilidad de asientos
    def sell_ticket(self, client_name, id_number, age, match_id, ticket_type):
        # Creando una instancia de Client con los datos del cliente
        client = Client(client_name, id_number, age)
        # Buscanco el partido 
        match = self.search_match_id(match_id)
        if not match:
            print("Partido no encontrado")
            return
        
        # Presio del ticket segun tipo 
        price = 35 if ticket_type.lower() == "general" else 75
        ticket = Ticket(ticket_type, price)
        
        # Si la cedula es un numero vampiro, aplica el descuento del 50%
        if Stadium.vampire_number(id_number):
            ticket.discount = price * 0.5
        
        # Asigna un asiento disponible
        seat = self.assign_seat(match.stadium)
        if not seat:
            print("No hay asientos disponibles")
            return
        
        # Asigna el asiento al boleto y cacula el subtotal, IVA y total
        ticket.seat = seat
        subtotal, tax, total = ticket.calculate_total()
        # Creando una ventana "sale" con los detalles y le agrega a la lista de ventas 
        ticket.confirm_sale(client, match, subtotal, tax, total)
        
    def assign_seat(self, stadium):
        return stadium.assign_seat()
    
    # Metodo para marcar asistencia
    def mark_attendance(self, sale_id):
        # Se recorre la lista "self.sales", que contiene todas las ventas realizadas.
        for sale in self.sales:
            if sale.id == sale_id:
                sale.attendance = True
                print(f"Asistencia marcada para {sale.client.name}")
                return
        print("Venta no encontrada")

    # Metodo para verificar asistencia al partido
    def check_attendance(self, match_id):
        # Se utiliza el método self.search_match_id(match_id) para encontrar el partido correspondiente al match_id proporcionado.
        match = self.search_match_id(match_id)
        if not match:
            print("Partido no encontrado")
            return
        attendance_list = [sale for sale in self.sales if sale.match.id == match_id and sale.attendance]
        return attendance_list
    
    def process_order(self, client_name, id_number, age, ordered_products):
        client = Client(client_name, id_number, age)
        total_cost = 0
        purchased_products = []

        for product_info in ordered_products:
            stadium = self.search_stadium_id(product_info['stadium_id'])
            if not stadium:
                print(f"Estadio con id {product_info['stadium_id']} no encontrado")
                continue

            for restaurant in stadium.restaurants:
                for product in restaurant.products:
                    if product.product_name == product_info['product_name']:
                        if product.alcoholic and age < 18:
                            print(f"{client.name} no puede comprar bebidas alcohólicas")
                            continue
                        if product.quantity < product_info['quantity']:
                            print(f"No hay suficiente cantidad de {product.product_name}")
                            continue
                        total_cost += product.price * product_info['quantity']
                        product.quantity -= product_info['quantity']
                        purchased_products.append(product)

        if self.is_perfect_number(id_number):
            discount = total_cost * 0.15
            total_cost -= discount
        else:
            discount = 0

        tax = total_cost * 0.16
        final_total = total_cost + tax  
        
        print(f"Resumen de compra para {client.name}:")
        print(f"Subtotal: {total_cost:.2f}")
        print(f"Descuento: {discount:.2f}")
        print(f"IVA: {tax:.2f}")
        print(f"Total: {final_total:.2f}")
        
        return purchased_products
    
    def is_perfect_number(self, number):
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number
    
pass 
