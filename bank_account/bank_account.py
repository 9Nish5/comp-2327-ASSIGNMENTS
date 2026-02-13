class BankAccount:
    """
    Represents a bank account,
    belonging to a specific client.
       
    """
    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        Initializes a BankAccount with Validation.

        Args:
            account_number (int): The unique bank account identifier.
            client_number (int): The identifier of the account owner.
            balance (float): The starting balance.

        Raises:
            ValueError: If account/client numbers are not integers.
       
        """
        # Validate integer types for account and client identifiers.
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance (client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

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
    
    def update_balance(self, amount: float):
        """
        Updates the account balance.

        Args:
            amount (float): The numeric amount to add (positive) or 
            subtract (negative).

        """
        try: 
            self.__balance += float(amount)
        except (ValueError, TypeError):
            # Requirements state: If invalid, do not update the balance.
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