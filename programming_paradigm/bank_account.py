class BankAccount:
    """
    A simple Bank Account class with basic operations:
    - deposit money
    - withdraw money
    - check balance
    """

    def __init__(self, balance=0):
        """Initialize account with a starting balance (default = 0)."""
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw money if sufficient balance exists."""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: {self.balance}")
