

class Transaction:
    def __init__(self, customer_account_id, transaction_type, account_id, amount, transaction_date):
        self.customer_account_id = customer_account_id
        self.transaction_type = transaction_type
        self.account_id = account_id
        self.amount = amount
        self.transaction_date = transaction_date

    

# new_transaction, list_transaction_for_account,  all get/set for attributes

    def get_new_transaction(self):
        return self.new_transaction


    def set_new_transaction(self, new_transaction):
        self.new_transaction = new_transaction 



    def get_list_transaction_for_account(self):
        return self.list_transaction_for_account


    def set_list_transaction_for_account(self, list_transaction_for_account):
        self.list_transaction_for_account = list_transaction_for_account 


    def get_customer_account_id(self):
        return self.customer_account_id


    def set_customer_account_id(self, customer_account_id):
        self.customer_account_id = customer_account_id 


    def get_transaction_type(self):
        return self.transaction_type


    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type 


    def get_account_id(self):
        return self.account_id


    def set_account_id(self, account_id):
        self.account_id = account_id 




    def get_amount(self):
        return self.amount


    def set_amount(self, amount):
        self.amount = amount 


    def get_transaction_date(self):
        return self.transaction_date


    def set_transaction_date(self, transaction_date):
        self.transaction_date = transaction_date 