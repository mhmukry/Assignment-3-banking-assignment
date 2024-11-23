

class Customer:
    def __init__(self, Customer_id, Customer_name, Customer_date_of_birth, Customer_address, Customer_phone_number,Customer_email ):
        self.Customer_id = Customer_id
        self.Customer_name = Customer_name
        self.Customer_date_of_birth = Customer_date_of_birth
        self.Customer_address = Customer_address
        self.Customer_phone_number = Customer_phone_number
        self.Customer_email = Customer_email
        
 
    def get_Customer(self):
        return self

    def print_Customer(self):
        print(f'Customer_id {self.Customer_id}') 
        print(f'Customer {self.Customer_name}')
        print(f'Customer date_of_birth {self.Customer_date_of_birth}') 
        print(f'Customer address {self.Customer_address}')
        print(f'Customer phone number {self.Customer_phone_number}') 
        print(f'Customer email {self.Customer_email}')

    def set_Customer(self, Customer_id, Customer_name, Customer_date_of_birth, Customer_address, Customer_phone_number,Customer_email ):
        self.Customer_id = Customer_id
        self.Customer_name = Customer_name
        self.Customer_date_of_birth = Customer_date_of_birth
        self.Customer_address = Customer_address
        self.Customer_phone_number = Customer_phone_number
        self.Customer_email = Customer_email   
'''

    def get_Customer_id(self):
        return self.Customer_id


    def set_Customer_id(self, Customer_id):
        self.Customer_id = Customer_id 


    def get_Customer_name(self):
        return self.Customer_name


    def set_Customer_name(self, Customer_name):
        self.Customer_name = Customer_name 


    def get_Customer_date_of_birth(self):
        return self.Customer_date_of_birth


    def set_Customer_date_of_birth(self, Customer_date_of_birth):
        self.Customer_date_of_birth = Customer_date_of_birth 


    def get_Customer_address(self):
        return self.Customer_address


    def set_Customer_address(self, Customer_address):
        self.Customer_address = Customer_address


    def get_Customer_phone_number(self):
        return self.Customer_phone_number


    def set_Customer_phone_number(self, Customer_phone_number):
        self.Customer_phone_number = Customer_phone_number


    def get_Customer_email(self):
        return self.Customer_email


    def set_Customer_email(self, Customer_email):
        self.Customer_email = Customer_email



    def get_new_customer(self):
        return self.new_customer


    def set_new_customer(self, new_customer):
        self.new_customer = new_customer



    def get_update_customer(self):
        return self.update_customer


    def set_update_customer(self, update_customer):
        self.update_customer = update_customer
     

# new_customer,update_customer, get_customer, set_customer, & all get/set for attributes

'''