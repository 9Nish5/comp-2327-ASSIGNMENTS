from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Represents the base interface for service charge calculation strategies.
    
    This class defines the standard interface that all concrete service
    charge strategies must implement.
    
    """
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charge(self, account: object) -> float:
        """
        Calculates the service charges for a specific bank account.
        
        Args:
            account (object): The bank accounnt for which the service
                              charge is being calculated.
        
        Returns:
            float: The calculated service charge amount.
            
        """
        pass
