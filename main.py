class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance):
        if account_number in self.accounts:
            print("\nAccount already exists.")
        else:
            self.accounts[account_number] = {
                'holder_name': holder_name,
                'balance': initial_balance
            }
            print(f"\nAccount created for {holder_name} with initial balance Rs.{initial_balance}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"\nDeposited Rs.{amount} into account {account_number}")
        else:
            print("\nAccount does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"\nWithdrew Rs.{amount} from account {account_number}")
            else:
                print(f"\nInsufficient funds in account {account_number}")
        else:
            print("\nAccount does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]['balance']
            print(f"\nAccount {account_number} has balance: Rs.{balance}")
        else:
            print("\nAccount does not exist.")


def main():
    bank = Bank()

    while True:
        print("\n\n====================  Basic Banking System  ====================")
        print("\nPlease choose one of the following options...")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, holder_name, initial_balance)

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)

        elif choice == '5':
            print("\n\t\tExiting the program. Goodbye!!!!!!!!!!!!!!!!!!!!")
            print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
