class Flight:
    def __init__(self, flight_id,source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self,flight):
        self.flights.append(flight)
        
    def search_by_city(self, city):
        result = [flight for flight in self.flights if city in (flight.source, flight.destination)]
        return result
        
    def search_from_city(self, source):
        result = [flight for flight in self.flights if flight.source == source]
        return result
        
    def search_between_cities(self, source, destination):
        result = [flight for flight in self.flights if flight.source == source and flight.destination == destination]
        return result

def print_flights(flights):
    if not flights:
        print("No flights found.")
        return
    print("Flight ID\tFrom\tTo\tPrice")
    for flight in flights:
        print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")

flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

while True:
    print("Welcome to Flight Searching System. Created By Karamraj Singh Anand (E22CSEU1123)")
    print("\nSearch Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        city = input("Enter the city: ")
        result = flight_table.search_by_city(city)
        print_flights(result)
    elif choice == 2:
        source = input("Enter the source city: ")
        result = flight_table.search_from_city(source)
        print_flights(result)
    elif choice == 3:
        source = input("Enter the source city: ")
        destination = input("Enter the destination city: ")
        result = flight_table.search_between_cities(source, destination)
        print_flights(result)
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")