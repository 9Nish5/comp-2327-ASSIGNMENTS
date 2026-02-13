from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """
    Represents an investment account where management fees 
    can be waived based on the account's age.
    """
    def __init__(self, account_number, client_number, balance, date_created, management_fee):
        """
        Initializes the InvestmentAccount with a management fee.
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

    def get_service_charges(self) -> float:
        """
        Calculates service charges. Management fee is waived if the 
        account is older than 10 years.
        """
        ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        
        if self.date_created <= ten_years_ago:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

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