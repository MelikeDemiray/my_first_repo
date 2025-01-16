#Question5: Create a "Customer" class and an "Account" class. Let the "Account" class 
#inherit from the "Customer" class and represent a customer's bank account information.

#Customer Class Features:
#"name" (customer name)
#"surname" (customer surname)
#"tc_identification" (customer TR ID number)
#"phone" (customer phone number)

#Account Class Properties:
#"customer" (a Customer object)
#"account_number" (account number)
#"balance" (account balance)

#Customer Class Method:
#"display_information()": Displays the customer's name, surname, TR ID number and telephone number.

#Account Class Methods:
#"deposit(self, amount)": A method that deposits a certain amount of money into the account.
#"money_check(self, amount)": A method that withdraws a certain amount of money from the account. However, if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
#"display_balance()": A method that displays the account balance.

#Create these two classes, then create a Customer object and an Account object, 
#add the customer information to the Account object, and perform account operations and view the results.


class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"\ncustomer name and surname: {self.name} {self.surname}\ncustomer T.C number: {self.tc}\ncustomer phone number: {self.phone}")

class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone, account_number, balance):
        super().__init__(name, surname, tc_identification, phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit successful!")

    def money_check(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Transaction successful!")

        else:
            print(f"\nYour account does not have sufficient balance. Please enter a different amount or deposit money into your account!")
    def display_balance(self):
        print(f"Your total account balance: {self.balance}")

Info = Account("Eren","Karaca", '123456', '05123456','789456456',100)

def menu(Info):
    while True:
        print("\n1- Deposit money 2- Withdraw money 3-View account balance 4-View account information  0-Exit")
        while True:
            try:
                choice = int(input("\nPlease select the operation you want to perform: "))
                if -1< choice <5:
                    break
                else:
                    print("invalid number please try again!")
            except ValueError:
                print("please enter a number!")

        if choice == 0:
            break
        elif choice == 1:
            amount = float(input("please enter amount to deposit: "))
            Info.deposit(amount)
        elif choice == 2:
            amount = float(input("please enter amount to withdraw: "))
            Info.money_check(amount)
        elif choice == 3:
            Info.display_balance()
        elif choice == 4:
            Info.display_information()

menu(Info)
        



  