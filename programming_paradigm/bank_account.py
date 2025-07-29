class BankAccount:
    """A simple bank account class that handles deposits, withdrawals, and balance display"""
    
    def __init__(self, initial_balance=0.0):
        """
        Initialize the bank account with an optional initial balance
        Args:
            initial_balance (float): Starting balance (default 0.0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account
        Args:
            amount (float): Amount to deposit
        """
        if amount > 0:
            self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw money from the account
        Args:
            amount (float): Amount to withdraw
        Returns:
            bool: True if withdrawal succeeded, False if insufficient funds
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")
