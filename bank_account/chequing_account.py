from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    
    Represents a chequing account with overdraft protection.
    
    """
    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate):
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

        

    def get_service_charges(self) -> float:
        """Calculates changes based on overdraft limit."""
        total_charge = (BankAccount.BASE_SERVICE_CHARGE+
                        (self.__overdraft_limit - self.balance)
                         * self.__overdraft_rate)
        if self.balance >= self.__overdraft_limit:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return total_charge
        
    def __str__(self):
        return (f"{super().__str__()}"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate:.2%} "
                f"Account Type: Chequing")