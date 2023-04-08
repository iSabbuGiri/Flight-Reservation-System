import pandas as pd
import pickle

class Flight:
    def check_duplicate_flight(self, flight_number):
        with open('storage/flights.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                return True
            else:
                for item in data:
                    if 'Flight Number' in item and flight_number in item['Flight Number']:
                        return False
            return True


    def search_flights(self, departure_location, arrival_location):
        found = []
        with open('storage/flights.dat', 'rb') as f:
            data = pickle.load(f)
            
        for item in data:
            if (item['Departure Location'] == departure_location) and (item['Arrival Location'] == arrival_location):
                found.append(item)
                
        if found == []:
            print('No results.')
        else:
            df = pd.DataFrame(found)
            print(df)    
    
    def list_flights(self):
        with open('storage/flights.dat', 'rb') as f:
            data = pickle.load(f)
            df = pd.DataFrame(data)
            print('\n')
            print(df)
            print('\n')
            
    def create_flight(self, flight_number, flight_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival):
        if self.check_duplicate_flight(flight_number):
            with open('storage/flights.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
                    
            data.append(
                {
                    'Flight Number': flight_number,
                    'Airline Name': flight_name,
                    'Departure Location': departure_location,
                    'Arrival Location': arrival_location,
                    'Scheduled Departure': scheduled_departure,
                    'Scheduled Arrival': scheduled_arrival
                }
            )

            with open('storage/flights.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Flight no. must be unique.')
            
    def update_flight(self, old_flight_number, flight_number, flight_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival):
        if self.check_duplicate_flight(flight_number):
            with open('storage/flights.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
                    
            for item in data:
                if old_flight_number in item['Flight No.']: 
                    item['Flight Number'] = flight_number
                    item['Flight Name'] = flight_name,
                    item['Departure Location'] = departure_location,
                    item['Arrival Location'] = arrival_location,
                    item['Scheduled Departure'] = scheduled_departure,
                    item['Scheduled Arrival'] = scheduled_arrival
                else:    
                    print('Flight does not exist.')

            with open('storage/flights.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Flight no. must be unique.')  

    def detail_flight(self, flight_number):
        with open('storage/flights.dat', 'rb') as f:
            data = pickle.load(f)
        
        found = False
        for item in data:
            if 'Flight Number' in item and item['Flight Number'] == flight_number:
                found = True
                df = pd.DataFrame([item])
                print(df)
                
                print('\n Seats:\n')
                with open('storage/seats.dat', 'rb') as f:
                    data = pickle.load(f)
                    if flight_number in data:
                        for seat in data[flight_number]['Seats']:
                            print('\n')
                            for key, value in seat.items():
                                print('{} : {}'.format(key, value))
                break
        
        if not found:
            print('Flight not found.')
           
                   
    def delete_flight(self, old_flight_number: str) -> None:
        with open('storage/flights.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        for item in data:
            if old_flight_number in item['Flight No.']: 
                del item
            else:
                print('Flight does not exist.')

        with open('storage/flights.dat', 'wb') as f:
            pickle.dump(data, f)
            
    
        

