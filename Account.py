

class Account:
    def __init__(self, account_id, account_number, account_type, account_name, account_opening_date, account_holder_name, rate_of_interest):
        self.account_id = account_id
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.account_opening_date = account_opening_date
        self.account_holder_name = account_holder_name
        self.current_balance = 0
        self.rate_of_interest = rate_of_interest

    



        
     
# open_account , close_account, get_account, set_account & all get/set for attributes

    def get_account(self):
        return self

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type


    def get_open_account(self):
        return self.open_account


    def set_open_account(self, open_account):
        self.open_account = open_account




    def get_close_account(self):
        return self.close_account 


    def set_close_account(self, close_account):
        self.close_account = close_account


    def deposit_amount(self, deposit_amount):
        self.current_balance += deposit_amount
        print("amount deposited")
        print(withdraw_amount)
        print("current balance")
        print(self.current_balance)

    def withdraw_amount(self, withdraw_amount):
        self.current_balance -= withdraw_amount
        print("amount withdrawn")
        print(withdraw_amount)
        print("current balance")
        print(self.current_balance)

'''


        def get_account_id(self):
            return self.account_id


        def set_account_id(self, account_id):
            self.account_id = account_id


        def get_account_number(self):
            return self.account_number


        def set_account_number(self, account_number):
            self.account_number = account_number


        def get_account_type(self):
            return self.account_type


        def set_account_type(self, account_type):
            self.account_type = account_type
'''
