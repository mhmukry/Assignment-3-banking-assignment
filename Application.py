from Account import Account
from Bank import Bank
from SavingsAccount import SavingsAccount
from ChequingAccount import ChequingAccount

class Application:
    def __init__(self):
        self.Account = None
        self.Bank = None


    def showMainMenu(self):
        account_list = []
        run_Menu = 1
        
        while (run_Menu == 1):
            print("Please select your choices: ")
            print("1: Select Account")
            print("2: Open Account")
            print("3: Exit")
            choice = int(input("Select your choice: "))
            if choice == 1:
                index = -1
                index = self.Bank.search_account(account_list)
                if index > -1:
                    account_list[index].print_Account()
                    self.showAccountMenu(account_list[index])
                else:
                    print(f'Requested account number : {account_number} not found')
                
           
            if choice == 2:
                account_type = input("Enter account type(Savings/Chequing):  ")
                self.Bank = Bank("Mukry's bank") 
                account_number = input("Enter account number:  ")
                current_balance = 0
                account_holder_name = input("Enter account holder name:  ")
                rate_of_interest = self.get_user_input_float( "Enter Rate of Interest (0-100):  ",  0.0,  100.00)
                self.Account=self.Bank.open_account(account_number, account_type,  account_holder_name, current_balance, rate_of_interest)                
                account_list.append(self.Account)
                print(f'Account number: {self.Account.account_number}')
                print(f'Account type: {self.Account.account_type}')


            if choice == 3:
                run_Menu = 0

    def showAccountMenu(self, Account):
        Account.print_Account()
        run_Menu = 1
        while (run_Menu == 1):
            print("Account Menu")
            print("1: Check Balance") 
            print("2: Deposit")    
            print("3: Withdraw")       
            print("4: Exit") 
            choice = int(input("Enter your choice: ")) 
            if choice == 1:
                print(f' current balance: {Account.current_balance}')

            if choice == 2:
                deposit_amount =  int(input(f'Enter amount to deposit'))
                Account.deposit(deposit_amount)

            if choice == 3:
                withdraw_amount =  int(input(f'Enter amount to withdraw'))
                Account.withdraw(withdraw_amount)
           
            if choice == 4:
                run_Menu = 0

    def get_user_input_float(self,  input_str,  min_value,  max_value):
        while (1):
            input_integer = float(input(input_str))
            if ((input_integer >= min_value) and (input_integer <= max_value)):
                return input_integer
            else:
                print("Incorrect value")


    def run(self):
        run_program = 1
        while (run_program == 1):
            print("1: show Main Menu")

            print("2: Exit")
            choice = int(input("Select your choice: "))
            if choice == 1:
                self.showMainMenu()
            if choice == 2:
                run_program = 0



if __name__ == "__main__":
    app = Application()
    app.run()

        