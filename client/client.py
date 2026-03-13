from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client:
    """
    Represents a bank client with personal and contact information.

    This class acts as an Observer in the Observer Pattern to recieve
    notifications regarding bank account activity.
    """
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a Client instance with validated attributes.

        Args:
            client_number (int): The unique identifier for the client.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Raises:
            ValueError: If the clinet_number is not an int.
                        If the names are blank.

        """

        # Validate client_number: Must be an integer.
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate first_name: Stip whitespace and check if blank.
        if not first_name.strip():
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name.strip()

        # Validate last_name: Strip whitespace and check if blank.
        if not last_name.strip():
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name.strip()

        # Validate email address
        try: 
            validate_email(email_address, check_deliverability = False)
            self.__email_address = email_address
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """Returns the client's unique number."""
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """Return's the client's first name"""
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """Returns the cliennt's last name."""
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """Returns the client's email address."""
        return self.__email_address
    
    def update(self, message: str) -> None:
        """
        Responds to a notification from a Subject by sending a simulated email.
        
        Args:
            message (str): The notification message to be included in the email.
        """
        current_time = datetime.now()
        subject = f"ALERT: Unusual Activity: {current_time}"
        email_message = (f"Notification for {self.__client_number: }"
                         f"{self.__first_name} {self.__last_name}: {message}")
        
        simulate_send_email(self.__email_address, subject, email_message)
    
    def __str__(self) -> str:
        """
        Returns a formatted string representation of the client.
        Format: Last, First[Number] - Email

        """
        return (f"{self.__last_name}, {self.__first_name} "
                f"[{self.__client_number}] - {self.__email_address}\n")
    
                  
