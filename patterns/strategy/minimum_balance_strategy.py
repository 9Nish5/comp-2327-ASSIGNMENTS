from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Represents a service charge strategy based on a minimum balance
    requirement.
    
    This strategy penalizes accounts that fall below a specific
    balance threshold.
    """

    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy with a minimum threshold.
        
        Args:
            minimum_balance (float): The balance required to avoid increased
            service charges.
        """
        self._minimum_balance = minimum_balance
    
    def calculate_service_charge(self, account: object) -> float:
        """
        Calculates services charges based on the account's current balance.

        If the balance is below the minimum threshold, the base service
        charge is doubled.

        Args:
            account (object): The bank account being evaluated.

        Returns:
            float: The total calculated service charge.
        """

        if account.balance >= self._minimum_balance:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE * 2
        