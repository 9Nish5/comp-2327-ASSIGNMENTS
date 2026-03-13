"""
Module representing an investment account.

"""
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """
    Represents an investment account where management fees 
    can be waived based on the account's age.
    """
    def __init__(self, account_number, client_number, balance, date_created, management_fee):
        """
        Initializes the InvestmentAccount and sets up its service charge strategy.
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

        self.__service_charge_strategy = ManagementFeeStrategy(self.__management_fee)

    def get_service_charges(self) -> float:
        """
        Calculates service charges by delegating to the management fee strategy.

        Returns:
            float: The service charge calculated by the strategy.
        """
        return self.__service_charge_strategy.calculate_service_charge(self)

    def __str__(self):
        """
        Returns a formatted string representing the InvestmentAccount.
        """
        ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        
        if self.date_created <= ten_years_ago:
            management_fee_display = "Waived"
        else:
            management_fee_display = f"${self.__management_fee:,.2f}"
            
        return (f"{super().__str__()}"
                f"Date Created: {self.date_created} "
                f"Management Fee: {management_fee_display} Account Type: Investment")