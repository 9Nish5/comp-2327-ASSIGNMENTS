from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Represents a service charge strategy for investment accounts.
    
    This strategy applies a mangement fee unless the account has been
    active for more than ten years.
    
    """

    def __init__(self, management_fee: float):
        """
        Initializes the ManagementFeeStrategy with a specific fee.

        Args:
            management_fee (float): The fee charges for account management.

        """

        self._management_fee = management_fee
        # The threshold for wiaving fees is ten years prior to the current date.
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def calculate_service_charge(self, account: object) -> float:
        """
        Calculates service charges based on the age of the account.

        The management fee is waived if the account's creation date is 
        older than the ten-year threshold.

        Args:
            account (object): The bank account being evaluated.

        Returns:
            float: The total calculated service charge.

        """
        if account.date_created <= self.TEN_YEARS_AGO:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE + self._management_fee
               