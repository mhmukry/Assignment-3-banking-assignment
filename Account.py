

class Account:
    def __init__(self, account_number, account_type,  account_holder_name, current_balance, rate_of_interest):
        self.account_number = account_number
        self.account_type = account_type
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance
        self.rate_of_interest = rate_of_interest


    def print_Account(self): 
        print(f'account_number {self.account_number}')
        print(f'account_type {self.account_type}') 
        print(f'account_holder_name {self.account_holder_name}') 
        print(f'current_balance {self.current_balance}') 
        print(f'rate_of_interest {self.rate_of_interest}')

    def deposit(self, amount_to_deposit):

        self.current_balance += amount_to_deposit
        print(f'Current balance {self.current_balance} after deposit of {amount_to_deposit}')
    

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_account_holder_name(self):
        return self.account_holder_name

    def set_account_holder_name(self, account_holder_name):
        self.account_holder_name = account_holder_name


    def get_account_number(self):
        return self.account_number


    def set_account_number(self, account_number):
        self.account_number = account_number


    def get_rate_of_interest(self):
        return self.rate_of_interest
    

    def set_rate_of_interest(self, rate_of_interest):
        self.rate_of_interest = rate_of_interest

    def get_current_balance(self):
        return self.current_balance
    

    def set_current_balance(self, current_balance):
        self.current_balance = current_balance
