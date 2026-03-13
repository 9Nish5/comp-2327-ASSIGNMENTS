class Subject:
    """
    Represents the base class for subjects in the Observer Patter.
    
    The Subject maintains a list of observers and provides methods to
    attach, detach and notify those observers of stage changes.
    
    """
    def __init__(self):
        """
        Initializes the Subject with an empty list of observers.

        """
        self._observers = []

    def attach(self, observer: object) -> None:
        """
        Adds an observer to the list of observers.
        
        Args:
            observer (object): The observer object to be attached.
        
        """
        self._observers.append(observer)
    
    def detach(self, observer: object) -> None:
        """
        Removes an observer from the list of observers.
        
        Args:
            observer (object): The observer object to be detached.
            
        """

        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Notifies all attached observers by calling their update method.
        
        Args:
            message (str): The message to send to all observers.
            
        """

        for observer in self._observers:
            observer.update(message)
