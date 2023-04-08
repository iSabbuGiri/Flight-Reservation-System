import pickle
import pandas as pd

class Customer:
    def __init__(self) -> None:
        self.customer_data_file = 'storage/customers.dat'
    
    def get_customer_data(self):
        is_empty = False
        data = None
        with open(self.customer_data_file, 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                is_empty = True
                
        return data, is_empty
                
    def get_customer_id(self, full_name, date_of_birth):
        return '{}_{}'.format(full_name, date_of_birth.replace('-', '_'))
    
    def retrieve_customer(self, full_name, date_of_birth, data):
        customer_id = self.get_customer_id(full_name, date_of_birth)
        if customer_id in data:
            return data[customer_id], True 
        return {}, False
    
    def list_customer(self):
        data, is_empty = self.get_customer_data()
        if is_empty:
            print('No customer data.')
        else:
            df = pd.DataFrame(data)
            print(df)
    
    def create_customer(self, full_name, date_of_birth, contact_number, email_address):
        go = True
        data, is_empty = self.get_customer_data()
        if not is_empty:
            _, exists = self.retrieve_customer(full_name, date_of_birth, data)
            if exists:
                go = False
        else:
            data = {}
                
        if go:
            payload = {
                self.get_customer_id(full_name, date_of_birth): {
                    'Full Name': full_name,
                    'Date of Birth': date_of_birth,
                    'Contact Number': contact_number,
                    'Email Address': email_address
                }   
            }
            
            data.update(payload)
            
            with open (self.customer_data_file, 'wb') as f:
                pickle.dump(data, f)
            
    def update_customer(self, customer_id, full_name, date_of_birth, contact_number, email):
        self.delete_customer(customer_id)
        self.create_customer(full_name, date_of_birth, contact_number, email)
            
    def search_customer(self, customer_id):
        data, is_empty = self.get_customer_data()
        if not is_empty:
            if customer_id in data:
                res = data[customer_id]
                print('\n')
                for key, value in res.items():
                    print('{} : {}'.format(key, value))
            else:
                print('Customer with the given ID does not exist.')
        else:
            print('No data.')
    
    def delete_customer(self, customer_id):
        data, is_empty = self.get_customer_data()
        if not is_empty:
            if customer_id in data:
                del data[customer_id]
                
                with open(self.customer_data_file, 'wb') as f:
                    pickle.dump(data, f)
            else:
                print('Customer with the given ID does not exist.')        
        else:
            print('No data.')
