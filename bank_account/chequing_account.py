"""
Module representing a chequing account with overdraft.
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    
    Represents a chequing account using the Strategy pattern for fees.
    
    """
    def __init__(self, account_number, client_number, balance, date_created,
                 overdraft_limit, overdraft_rate):
        """
        Initializes the ChequingAccount and sets up its service charge strategy.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        self.__overdraft_limit = float(overdraft_limit)
        self.__overdraft_rate = float(overdraft_rate)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

        # Create the private strategy attribute
        self.__service_charge_strategy = OverdraftStrategy(self.__overdraft_limit, 
                                                           self.__overdraft_rate)

    def get_service_charges(self) -> float:
        """
        Calculates service charges by delegating to the overdraft strategy.

        Returns:
            float: The service charge calculated by the strategy.

        """
        return self.__service_charge_strategy.calculate_service_charge(self)
        
    def __str__(self):
        return (f"{super().__str__()}"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate:.2%} "
                f"Account Type: Chequing")