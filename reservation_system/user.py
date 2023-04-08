from flight import Flight
from seat import Seat
from reservation import Reservation
from customer import Customer

class Client:
    def __init__(self):
        self.run = True


    def ready(self):
        self.help()
        self.flight_main()

    def help(self):
        print('Welcome to the convenient Flight Booking Service.\n')
        print('Enter S for search flights.')
        print('Enter D for flight details.')  
        print('Enter B to go back.')

    def flight_main(self):
        choose = input('choose : ')
        if choose == 'A':
            self.flight_search()
        elif choose == 'B':
            self.detail_flight()
        elif choose == 'R':
            self.ready()

    def flight_search(self):
        departure_location = input('Enter departure location : ')
        arrival_location = input('Enter arrival location : ')
        flight = Flight()
        flight.search(departure_location, arrival_location)

    def detail_flight(self):
        flight_number = input('Enter flight number : ')
        flight = Flight()
        flight.detail_flight(flight_number)


class Staff:
    def __init__(self):
        self.run = True
        
    def ready(self):
        self.help()
        self.main()
        
    def end(self):
        print('\nProgram stopped.')
        self.run = False
    
    def help(self):
        print('Welcome to the convenient Flight Booking Service.\n')
        print('Enter F for Flights.')
        print('Enter S for Seats.')
        print('Enter C for Customers.')
        print('Enter R for Reservations.')
        print('Enter E to exit.')
    
    def main(self):
        choose = input('Choose: ')
        if choose == 'F':
            self.flight_main()   
        elif choose == 'S':
            self.seat()
        elif choose == 'C':
            self.customer()
        elif choose == 'R':
            self.reservation()        
        elif choose == 'E':
            self.end()
        else:
            print('Incorrect input. Please try again with a valid choice.\n')
            
        if self.run:
            self.ready()
        
    def flight_main(self):
        print('\n')
        print('Enter L to list flights.')
        print('Enter C to create a flight.')
        print('Enter U to update a flight.')
        print('Enter D to delete a flight.')
        print('Enter S to search a flight.')
        print('Enter V to view flight details.')
        print('Enter B to go back.')
        
        choose = input('Choose : ')
        if input == 'L':
            self.list_flights()
        elif choose == 'C':
            self.create_flight()
        elif choose == 'U':
            self.update_flight()
        elif choose == 'D':
            self.delete_flight()
        elif choose == 'S':
            self.search_flights()
        elif choose == 'V':
            self.detail_flight()
        elif choose == 'B':
            self.ready()
            
        if self.run:
            self.flight_main()
        
    def list_flight(self):
        flight = Flight()
        flight.list_flights()   
        
    def flight_detail(self):
        flight_number = input('Enter flight number : ')
        flight = Flight()
        flight.detail_flight(flight_number)   
          
    def create_flight(self):
        flight_number = input('Enter flight : ')
        airline_name = input('Enter airline name : ')
        departure_location = input('Enter Departure location : ')
        arrival_location = input('Enter Arrival location : ')
        scheduled_departure = input('Enter departure time (YYYY-MM-DD) : ')
        scheduled_arrival = input('Enter arrival time (YYYY-MM-DD) : ')
        flight = Flight()
        flight.create_flight(flight_number, airline_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival)
        
    def update_flight(self):
        old_flight_number = input('Enter a Flight number to update :')
        flight_number = input('Enter Flight Number : ')
        airline_name = input('Enter Airline Name : ')
        departure_location = input('Enter Departure location : ')
        arrival_location = input('Enter Arrival location : ')
        scheduled_departure = input('Enter departure time (MM-DD-YYYY) : ')
        scheduled_arrival = input('Enter arrival time (MM-DD-YYYY) : ')
        flight = Flight()
        flight.update_flight(old_flight_number, flight_number, airline_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival)
        
    def delete_flight(self):
        old_flight_number = input('Enter a Flight number to delete :')
        flight = Flight()
        flight.delete_flight(old_flight_number)
        
    def flight_search(self):
        departure_location = input('Enter departure_location : ')
        arrival_location = input('Enter arrival_location : ')
        flight = Flight()
        flight.search_flights(departure_location, arrival_location)

    def reservation(self):
        print('\n')
        print('Enter L to list reservation.')
        print('Enter C to create a reservation.')
        print('Enter U to update a reservation.')
        print('Enter D to delete a reservation.')
        print('Enter S to search a reservation.')
        print('Enter V to view reservation details.')
        print('Enter B to go back.')
        
        choose = input('\nchoose : ')
        if choose == 'L':
            self.list_reservation()
        elif choose == 'C':
            self.create_reservation()
        elif choose == 'U':
            self.update_reservation()
        elif choose == 'D':
            self.delete_reservation()
        elif choose == 'S':
            self.search_reservation()
        elif choose == 'R':
            self.reservation_detail()
        elif choose == 'Q':
            self.ready()
            
        if self.run:
            self.reservation()
    
    def list_reservation(self):
        reservation = Reservation()
        reservation.list_reservations()
        
    def create_reservation(self):
        flight_number = input('Enter flight number : ')
        customer_id = input('Enter customer ID : ')
        seat_number = input('Enter seat number : ')
        arrival_date = input('Enter arrival date (YYYY-MM-DD) : ')
        reservation = Reservation()
        reservation.create_reservation(flight_number, customer_id, seat_number, arrival_date)
        
    def update_reservation(self):
        id = input('Enter reservation ID')
        flight_number = input('Enter flight number : ')
        customer_id = input('Enter customer ID : ')
        seat_number = input('Enter seat number : ')
        arrival_date = input('Enter arrival date (MM-DD-YYYY) : ')
        reservation = Reservation()
        reservation.update_reservation(id, flight_number, customer_id, seat_number, arrival_date)
        
    def delete_reservation(self):
        id = input('Enter reservation ID :')
        reservation = Reservation()
        reservation.delete_reservation(id) 
    
    def search_reservation(self):
        customer_name = input('Enter customer name : ')
        reservation = Reservation()
        reservation.search_reservation(customer_name)
        
    def reservation_detail(self):
        id = input('Enter reservation ID : ')
        reservation = Reservation()
        reservation.detail_reservation(id)

    def customer(self):
        print('\n')
        print('Enter L to list customers.')
        print('Enter C to create a customer.')
        print('Enter U to update a customer.')
        print('Enter D to delete a customer.')
        print('Enter S to search a customer.')
        print('Enter B to go back.')
        
        choose = input('\nchoose : ')
        if choose == 'L':
            self.list_customer()
        elif choose == 'C':
            self.create_customer()
        elif choose == 'U':
            self.update_customer()
        elif choose == 'D':
            self.delete_customer()
        elif choose == 'S':
            self.search_customer()
        elif choose == 'B':
            self.ready()
            
        if self.run:
            self.customer()

    def list_customer(self):
        customer = Customer()
        customer.list_customer()
        
    def create_customer(self):
        full_name = input("Enter Full Name : ")
        date_of_birth = input("Enter Date of Birth (YYYY-MM-DD) : ")
        contact_number = input("Enter Phone Number : ")
        email_address = input("Enter Email : ")
        customer = Customer()
        customer.create_customer(full_name, date_of_birth, contact_number, email_address)
        
    def update_customer(self):
        id = input('Enter customer id : ')
        full_name = input("Enter Full Name : ")
        date_of_birth = input("Enter Date of Birth (YYYY-MM-DD) : ")
        contact_number = input("Enter Phone Number : ")
        email_address = input("Enter Email : ")
        customer = Customer()
        customer.update_customer(id, full_name, date_of_birth, contact_number, email_address)
        
    def delete_customer(self):
        id = input('Enter customer ID : ')
        customer = Customer()
        customer.delete_customer(id)
    
    def search_customer(self):
        id = input('Enter customer ID : ')
        customer = Customer()
        customer.search_customer(id)
            
        
    def seat(self):
        print('Enter C to create a seat.')
        print('Enter E to exit.')
        
        choose = input('choose : ')
        if choose == 'C':
            self.create_seat()
        elif choose == 'e':
            self.end()
            
        if self.run:
            self.ready()
        
    def list_seats(self):
        seat = Seat()
        seat.list()   
          
    def create_seat(self):
        flight_number = input('Enter flight : ')
        seat_name = input('Enter seat : ')
        seat_type = input('Enter seat type : ')
        seat = Seat()
        seat.add_seat(flight_number, seat_name, seat_type)

class UI:
    def __init__(self, user_type):
        self.user_type = user_type
    
    def ready(self):
        if self.user_type == 'client':
            client = Client()
            client.ready()
        elif self.user_type == 'staff':
            staff = Staff()
            staff.ready()
        else:
            raise Exception("Invalid user type.")
