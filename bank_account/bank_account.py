from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject


class BankAccount(Subject, ABC):
    
    """
    Represents a bank account,
    belonging to a specific client.

    Abstract Base Class for all bank account types.
       
    """
    LOW_BALANCE_LEVEL = 50.0
    LARGE_TRANSACTION_THRESHOLD = 10000.0
    
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """
        Initializes a BankAccount with Validation.

        Args:
            account_number (int): The unique bank account identifier.
            client_number (int): The identifier of the account owner.
            balance (float): The starting balance.
            date_created (date): The date the account was opened.

        Raises:
            ValueError: If account/client numbers are not integers.
       
        """
        # Invoking Subject's __init__ to initialize the observer list
        super().__init__()

        # Validate integer types for account and client identifiers.
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance (client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Date Validation
        if isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()

        # Validate balance: Convert to float, default to 0.0 on faliure
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

    @property
    def account_number(self) -> int:
        """Returns the account number."""
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """Returns the associated client number."""
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """Returns the current balance."""
        return self.__balance
    
    @property
    def date_created(self):
        """date: Returns the date the account was created."""
        return self.__date_created
    
    def update_balance(self, amount: float) -> None:
        """
        Updates the account balance and notifies observers if thresholds
        are met.

        Args:
            amount (float): The amount to add to or subtract from the balance.
        """
        self.__balance += amount

        # Check for low balance level
        if self.__balance < BankAccount.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:,.2f}: "
                        f"on account {self.__account_number}.")
        
        if abs(amount) > BankAccount.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large Transaction ${abs(amount):,.2f}: "
                        f"on account {self.__account_number}.")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges for the account.
        Must be implemented by subclass.
        """
        pass    
    

    def deposit(self, amount: float):
        """
        Validates and processes a deposit.
        
        Args:
            amount (float): The amount to deposit. Must be numeric and positive.
            
        Raises:
            ValueError: If amoutn is non-numeirc or <= 0.
            
        """
        try:
            value = float(amount)
        except (ValueError, TypeError): 
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if value <= 0:
            # Currency formatting
            if value < 0:
                positive_value = value * -1
                formatted_value = f"-${positive_value:,.2f}"
            else:
                formatted_value = f"${value:,.2f}"
            raise ValueError(f"Deposit amount: {formatted_value} must be positive.")
        
        self.update_balance(value)

    def withdraw(self, amount: float):
        """
        Validates and processes a withdrawal.

        Args:
            amount (float): The amount to withdraw. Must be numeric, positive,
                            and <= balance.

        Raises: 
            ValueError: For invalid types, negative amounts,
                        insufficient funds.

        """
        
        try:
            value = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if value <= 0:
            if value < 0:
                # Multiply by -1 to make it positive for formatting
                positive_value = value * -1
                formatted_amount = f"-${positive_value:,.2f}"
            raise ValueError(f"Withdraw amount: {formatted_amount} must be positive.")
        
        if value > self.__balance:
            raise ValueError(f"Withdraw amount: ${value:,.2f} must not exceed the " 
                             f"account balance: ${self.__balance:,.2f}.")
        
        # Withdrawals are passed as negative values to update_balance.
        self.update_balance(-value)

    def __str__(self) -> str:
        """

        Returns a formatted string of the account details.
        
        """
        return (f"Account Number: {self.__account_number} "
                f"Balance: ${self.__balance:,.2f}\n")