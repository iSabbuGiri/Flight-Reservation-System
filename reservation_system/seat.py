import pickle

class Seat:
    def check_flight_existence(self, flight_number):
        with open('storage/flights.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                return False
            else:
                for item in data:
                    if flight_number == item.get('Flight Number'):
                        return True
                return False

        
    def add_seat(self, flight_number, seat, seat_type):
        if self.check_flight_existence(flight_number):
            with open('storage/seats.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = {}    
                    
            if flight_number in data:
                data[flight_number]['Seats'].append({
                    'Name': seat,
                    'Reserved': 0,
                    'Type': seat_type
                })
            else:
                data.update({
                    flight_number: {
                        'Seats': [{
                            'Name': seat,
                            'Reserved': 0, 
                            'Type': seat_type
                        }]
                    }
                })
                
            with open('storage/seats.dat', 'wb') as f:
                data = pickle.dump(data, f)
        else:
            print('Flight not found. Please check the flight number.')


          