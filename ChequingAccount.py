from Account import Account

class ChequingAccount(Account):
    pass
    def __init__(self, account_number, account_type,  account_holder_name, current_balance, rate_of_interest):
        self.account_number = account_number
        self.account_type = account_type
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance
        self.rate_of_interest = rate_of_interest
        self.over_draft_Limit = 500


    def withdraw(self, amount_to_withdraw):
        if ((self.current_balance + self.over_draft_Limit) >= amount_to_withdraw ):
            self.current_balance -= amount_to_withdraw
            print(f'Current balance {self.current_balance} after withdrawal of {amount_to_withdraw}')
        else:
            print(f' Over draft limit: {self.over_draft_Limit} , Current balance: {self.current_balance} ')
            print(f' Could not withdraw the requested amount of: {amount_to_withdraw}, Current balance: {self.current_balance} ')

