import os
import json

class Account:
    """Represents a bank account."""

    def __init__(self, account_number: int, name: str, balance: float):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        """Convert account details to a dictionary for file handling."""
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
        }

    @staticmethod
    def from_dict(data):
        """Create an Account object from a dictionary."""
        return Account(data["account_number"], data["name"], data["balance"])


class Bank:
    """Manages multiple accounts and banking operations."""

    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def create_account(self, name: str, initial_deposit: float):
        """Create a new account with a unique account number."""
        if initial_deposit < 0:
            print("Initial deposit must be a non-negative value.")
            return
        account_number = len(self.accounts) + 1
        while account_number in self.accounts:  # Ensure unique account numbers
            account_number += 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number: int):
        """View details of an account by account number."""
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
        else:
            print(
                f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance:.2f}"
            )

    def deposit(self, account_number: int, amount: float):
        """Deposit money into an account."""
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
        elif amount <= 0:
            print("Deposit amount must be positive.")
        else:
            account.balance += amount
            self.save_to_file()
            print(f"Deposit successful! New Balance: {account.balance:.2f}")

    def withdraw(self, account_number: int, amount: float):
        """Withdraw money from an account."""
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > account.balance:
            print("Insufficient balance.")
        else:
            account.balance -= amount
            self.save_to_file()
            print(f"Withdrawal successful! New Balance: {account.balance:.2f}")

    def transfer(self, from_account: int, to_account: int, amount: float):
        """Transfer money from one account to another."""
        sender = self.accounts.get(from_account)
        receiver = self.accounts.get(to_account)

        if not sender:
            print("Sender account not found.")
        elif not receiver:
            print("Receiver account not found.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > sender.balance:
            print("Insufficient balance in sender's account.")
        else:
            sender.balance -= amount
            receiver.balance += amount
            self.save_to_file()
            print(
                f"Transfer successful! {amount:.2f} transferred from Account {from_account} to Account {to_account}."
            )

    def save_to_file(self):
        """Save all account details to a file."""
        with open(self.filename, "w") as file:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(data, file)

    def load_from_file(self):
        """Load all account details from a file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.accounts = {
                        int(acc_num): Account.from_dict(acc)
                        for acc_num, acc in data.items()
                    }
            except (json.JSONDecodeError, KeyError):
                print("Error loading account data. Starting with an empty bank.")
                self.accounts = {}


def main():
    bank = Bank()

    while True:
        print("\n--- Welcome to the Bank Application ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter your name: ")
                initial_deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, initial_deposit)

            elif choice == 2:
                account_number = int(input("Enter account number: "))
                bank.view_account(account_number)

            elif choice == 3:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit(account_number, amount)

            elif choice == 4:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(account_number, amount)

            elif choice == 5:
                from_account = int(input("Enter sender account number: "))
                to_account = int(input("Enter receiver account number: "))
                amount = float(input("Enter transfer amount: "))
                bank.transfer(from_account, to_account, amount)

            elif choice == 6:
                print("Thank you for using the Bank Application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid input.")


if __name__ == "__main__":
    main()
