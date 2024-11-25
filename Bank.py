from Account import Account
from SavingsAccount import SavingsAccount
from ChequingAccount import ChequingAccount


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.Account = None



    def open_account(self, account_number, account_type,  account_holder_name, current_balance, rate_of_interest):
        if account_type == "Savings":
            self.Account = SavingsAccount(account_number, account_type,  account_holder_name, current_balance, rate_of_interest)
            print(f'Account Type {self.Account.get_account_type()}')


        if account_type == "Chequing":
            self.Account = ChequingAccount(account_number, account_type,  account_holder_name, current_balance, rate_of_interest)
            print(self.Account.get_account_type())
            
        return self.Account
        #print(Account.acount_holder_name)


    def search_account(self,account_list):
        i = 0
        print("Please select account from the following list: ")
        while i < len(account_list):
            print(f'Account number: {account_list[i].account_number}     Account type: {account_list[i].account_type}')
            i = i + 1
        account_number = input("Enter account number: ")
        i = 0
        index = -1
        while i < len(account_list):
            if account_list[i].account_number == account_number:
                index = i    
            i = i + 1
        if index > -1:
            account_list[index].print_Account()
            return index
        else:
            print(f'Requested account number : {account_number} not found')
            return -1

        







'''

    def get_open_account(self):
        return self.open_account
    
    def set_open_account(self, open_account):
        self.open_account = open_account





    def get_search_account(self):
        return self.get_search_account
    
    def set_search_account(self, search_account)

'''    