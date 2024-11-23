from Account import Account


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.Account = None



    def open_account(self):
        account_id = input("Enter account ID")
        account_number = input("Enter account number")
        account_type = input("Enter account type")
        account_name = input("Enter account name")
        account_opening_date = input("Enter account opening date")
        account_holder_name = input("Enter account holder name")
        rate_of_interest = input("Enter rate of interest")  
        self.Account = Account(account_id, account_number, account_type, account_name, account_opening_date, account_holder_name, rate_of_interest)
        print(self.Account.get_account_type())
        #print(Account.acount_holder_name)


    def search_account(self):
         account_id = input("Enter account ID")
        







'''

    def get_open_account(self):
        return self.open_account
    
    def set_open_account(self, open_account):
        self.open_account = open_account





    def get_search_account(self):
        return self.get_search_account
    
    def set_search_account(self, search_account)

'''    