from Account import Account
from Customer import Customer
from Transaction import Transaction
from Bank import Bank

class Application:
    def __init__(self):
        self.Account = None
        self.Transaction = None
        self.Customer = None
        self.Bank = None


    def get_user_input(self):
        Customer_id = 0
        Customer_list = []
        while (1):
            print("Please select your choices: ")
            print("1: Add new customer")
            print("2: Update customer")
            choice = int(input("Select your choice: "))
            '''while (1):
                print("Please select your choices: ")
                print("1: Add new customer")
                print("2: Update customer")
                print("3: Transaction")
                print("4: Create account")
                choice = int(input("Select your choice: "))
                if choice == 1:
                    Customer_name = input("Enter customer name")
                    Customer_date_of_birth = input("Enter customer date of birth")
                    Customer_address = input("Enter customer address")
                    Customer_phone_number = input("Enter customer phone number")
                    Customer_email = input("Enter customer email")
                    self.Customer = Customer(Customer_id + 1, Customer_name, Customer_date_of_birth, Customer_address, Customer_phone_number,Customer_email)
                    #Customer.get_Customer(self.Customer)
                    Customer_list.append(self.Customer)

                if choice == 2:
                    i = 0
                    print("Please select customers from the following list:")
                    while i < len(Customer_list):
                        print(Customer_list[i].Customer_name)
                        i = i + 1
                    Customer_name = input("Enter customer name")
                    i = 0
                    index = 0
                    while i < len(Customer_list):
                        if Customer_list[i].Customer_name == Customer_name:
                            index = i    
                        i = i + 1
                    Customer_list[index].print_Customer()   
                
                if choice == 3:
                    customer_account_id = input("Enter customer account ID")
                    transaction_type = input("Enter transaction type")
                    account_id = input("Enter account ID")
                    amount = input("Enter amount")
                    transaction_date = input("Enter transaction date")     

                if choice == 4:
                    self.Bank = Bank("abc bank") 
                    self.Bank.open_account()
                '''
    def run(self):
        self.showMainMenu()
        self.showAccountMenu()

if __name__ == "__main__":
    app = Application()
    app.run()

        