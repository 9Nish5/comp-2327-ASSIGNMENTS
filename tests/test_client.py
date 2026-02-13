"""Unit testing for the Client class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client

class testClient(unittest.TestCase):
    """
    
    Unit tests for the Client class to ensure proper encapsulation
    and validation.
    
    """
    def test_init_valid_data_sets_attributes(self):
        """
        Valid inputs are set correctly

        """
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
       
        self.assertEqual(1010, client._Client__client_number)
        self.assertEqual("Susan", client._Client__first_name)

    def test_init_invalid_client_number_raises_exception(self):
        """Non-integer client number raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Client("ABC", "Susan", "Clark", "susan@test.com")

        self.assertEqual("Client number must be an integer.", str(context.exception))
        

    def test_init_blank_first_name_raises_esxcpetion(self):
        """Blank first name raises ValueError"""

        with self.assertRaises(ValueError) as context:
            Client(1010, "", "Clark", "susan@test.com")

        self.assertEqual("First name cannot be blank.", str(context.exception))
        

    def test_init_blank_last_name_raises_esxcpetion(self):
        """Blank last name raises ValueError"""

        with self.assertRaises(ValueError) as context:
            Client(1010, "Susan", "  ", "susan@test.com")

        self.assertEqual("Last name cannot be blank.", str(context.exception))
        

    def test_init_invalid_email_uses_default(self):
        """Invalid email sets default."""

        # Act
        client = Client(1010, "Susan", "Clark", "not-email")

        # ASSERT
        self.assertEqual("email@pixell-river.com", client._Client__email_address)
        
    def test_accessor_return_attribute_values(self):
        """Test case 6-9"""
        client = Client(1010, "Susan", "Clark", "susan@test.com")

        self.assertEqual(client.client_number, 1010)
        self.assertEqual(client.first_name, "Susan")
        self.assertEqual(client.last_name, "Clark")
        self.assertEqual(client.email_address, "susan@test.com")

    def test_str_representation(self):
        """Test 10"""

        # ARRANGE
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

        excepted = "Clark, Susan [1010] - susanclark@pixell.com\n"

        # ASSERT
        self.assertEqual(str(client), excepted)

if __name__ == "__main__":
    unittest.main()