import pandas as pd
import pickle
import uuid

class Reservation:
    def list_reservations(self):
        with open('storage/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
               print('Data not found.')
            else:
                if len(data) == 0:
                    print('Data not found.')
                else:
                    df = pd.DataFrame(data)
                    print('\n')
                    print(df)
                    print('\n')
            
    def detail_reservation(self, id):
        with open('storage/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                print('Data not found.')
            else:
                if id in data:
                    for key, value in data[id].items():
                        print('{} : {}'.format(key, value))
                        
    def search_reservation(self, customer):
        res = {}
        with open('storage/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
        for key, value in data.items():
            if value['Customer'] == customer:
                res.update({
                    key: value
                })
                
        df = pd.DataFrame(res)
        print('\n{}'.format(df))
            
    def create_reservation(self, flight_number, customer, seat_number, arrival_date):
        with open('storage/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                
        data.update({
            str(uuid.uuid4()): {
                'Flight Number': flight_number,
                'Customer': customer,
                'Seat Number': seat_number,
                'Arrival_Date': arrival_date
            }
        })

        with open('storage/reservations.dat', 'wb') as f:
            pickle.dump(data, f)
            
    def update_reservation(self, id, flight_number, customer_name, seat_number, arrival_date):
        with open('storage/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                
        if id in data:
            data[id]['Flight Number'] = flight_number
            data[id]['Customer Name'] = customer_name
            data[id]['Seat Number'] = seat_number
            data[id]['Arrival Date'] = arrival_date

            with open('storage/reservations.dat', 'wb') as f:
                pickle.dump(data, f)   
        else:
            print('No reservation found with the provided ID.')  
                   
    def delete_reservation(self, id):
        with open('storage/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                
        if id in data:
            del data[id]
        else:
            print('No reservation found with the provided ID.')

        with open('storage/reservations.dat', 'wb') as f:
            pickle.dump(data, f)
