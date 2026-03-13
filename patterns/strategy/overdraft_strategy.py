from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Represents a service charge strategy that accounts for overdraft protection.
    
    This strategy calculates fees based on whether the account balance has
    fallen below the designed overdraft limit.
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy with a limit and rate.

        Args:
            overdraft_limit (float): The balance threshold where overdraft
                                     feese begin to apply.
            overdraft_rate (float): The rate used to calculate the 
                                    overdraft fee.
        """
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charge(self, account: object) -> float:
        """
        Calculates service charges based on the account balance and overdraft 
        parameters.

        If the account balance is above the overdraft limit, only the base
        service charge is returned. Otherwise, an additional fees is calculated
        based on the overdraft fee.

        Args:
            account (object): The bank account being evaluated.

        Returns:
            float: The total calculated service charge.
        """
        if account.balance >= self._overdraft_limit:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            return (ServiceChargeStrategy.BASE_SERVICE_CHARGE + 
                    self._overdraft_limit - account.balance) * self._overdraft_rate

        