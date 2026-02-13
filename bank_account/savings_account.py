from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    Represents a savings account that penalizes balances below a minimum.
    """
    
    def __init__(self, account_number, client_number, balance, date_created, minimum_balance):
        """
        Initializes the SavingsAccount with a minimum balance requirement.
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        # Validation: ensure minimum_balance is a float or default to 50.0
        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50.0

    def get_service_charges(self) -> float:
        """
        Calculates service charges. If balance is below minimum, 
        the base service charge is doubled.
        """
        if self.balance >= self.__minimum_balance:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE * 2

    def __str__(self):
        """
        Returns a formatted string representing the SavingsAccount.
        """
        return (f"{super().__str__()}"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} "
                f"Account Type: Savings")