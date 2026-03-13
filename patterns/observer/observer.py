from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Rpresents the abstract base class for all observer objects.
    
    This class defines the interface for concrete observers that must 
    be notified of changes in a subject.
    
    """
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Abstract method to be implemented by concrete observers to recieve 
        notifications from subjects.
        
        Args:
            message (str): The notification message sent by the subject.

        Returns:
            None
        """
        pass
