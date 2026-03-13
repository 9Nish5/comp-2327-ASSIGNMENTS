from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    Represents a savings account that penalizes balances below a minimum.
    """
    
    def __init__(self, account_number, client_number, balance, date_created, minimum_balance):
        """
        Initializes the SavingsAccount and sets up its service charge strategy.
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        # Validation: ensure minimum_balance is a float or default to 50.0
        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50.0

        self.__service_charge_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def get_service_charges(self) -> float:
        """
        Calculates service charges by delegating to the minimum balance strategy.

        Returns:
            float: The service charge calculated by the strategy.
        """
        return self.__service_charge_strategy.calculate_service_charge(self)

    def __str__(self):
        """
        Returns a formatted string representing the SavingsAccount.
        """
        return (f"{super().__str__()}"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} "
                f"Account Type: Savings")