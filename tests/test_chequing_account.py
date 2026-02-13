import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
    """
    Unit tests for the ChequingAccount class.
    Tests polymorphic behavior and attribute validation.
    """

    def test_init_attributes_set_to_input_values(self):
        """Test Case 1: Ensures all attributes are set correctly via the constructor."""
        # Arrange
        account_number = 12345
        client_number = 1010
        balance = 500.0
        date_created = date(2023, 1, 1)
        overdraft_limit = -150.0
        overdraft_rate = 0.05

        # Act
        chequing_account = ChequingAccount(account_number, client_number, balance, 
                                           date_created, overdraft_limit, overdraft_rate)

        # Assert
        # Using name mangling to check private attributes
        self.assertEqual(account_number, chequing_account._BankAccount__account_number)
        self.assertEqual(client_number, chequing_account._BankAccount__client_number)
        self.assertEqual(balance, chequing_account._BankAccount__balance)
        self.assertEqual(date_created, chequing_account.date_created)
        self.assertEqual(overdraft_limit, chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(overdraft_rate, chequing_account._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit_type_sets_default(self):
        """Test Case 2: Ensures invalid overdraft limit type defaults to -100.0."""
        # Arrange
        invalid_overdraft_limit = "invalid_type"

        # Act
        chequing_account = ChequingAccount(123, 101, 500.0, date.today(), 
                                           invalid_overdraft_limit, 0.05)

        # Assert
        self.assertEqual(-100.0, chequing_account._ChequingAccount__overdraft_limit)

    def test_init_invalid_overdraft_rate_type_sets_default(self):
        """Test Case 3: Ensures invalid overdraft rate type defaults to 0.05."""
        # Arrange
        invalid_overdraft_rate = "invalid_type"

        # Act
        chequing_account = ChequingAccount(123, 101, 500.0, date.today(), 
                                           -100.0, invalid_overdraft_rate)

        # Assert
        self.assertEqual(0.05, chequing_account._ChequingAccount__overdraft_rate)

    def test_init_invalid_date_created_type_sets_today(self):
        """Test Case 4: Ensures invalid date created type defaults to date.today()."""
        # Arrange
        invalid_date = "2023-01-01" # String instead of date object
        expected_date = date.today()

        # Act
        chequing_account = ChequingAccount(123, 101, 500.0, invalid_date, -100.0, 0.05)

        # Assert
        self.assertEqual(expected_date, chequing_account.date_created)

    def test_get_service_charges_balance_greater_than_overdraft_limit(self):
        """Test Case 5: Service charge should be BASE_SERVICE_CHARGE when balance > limit."""
        # Arrange
        overdraft_limit = -100.0
        balance = 50.0
        chequing_account = ChequingAccount(123, 101, balance, date.today(), 
                                           overdraft_limit, 0.05)

        # Act
        actual_service_charge = chequing_account.get_service_charges()

        # Assert
        self.assertEqual(0.50, actual_service_charge)

    def test_get_service_charges_balance_less_than_overdraft_limit(self):
        """Test Case 6: Service charge should include overdraft fees when balance < limit."""
        # Arrange
        # Formula: 0.50 + (-100 - -600) * 0.05 = 25.50
        overdraft_limit = -100.0
        balance = -600.0
        overdraft_rate = 0.05
        chequing_account = ChequingAccount(123, 101, balance, date.today(), 
                                           overdraft_limit, overdraft_rate)

        # Act
        actual_service_charge = chequing_account.get_service_charges()

        # Assert
        self.assertEqual(25.50, round(actual_service_charge, 2))

    def test_get_service_charges_balance_equal_to_overdraft_limit(self):
        """Test Case 7: Service charge should be BASE_SERVICE_CHARGE when balance == limit."""
        # Arrange
        overdraft_limit = -100.0
        balance = -100.0
        chequing_account = ChequingAccount(123, 101, balance, date.today(), 
                                           overdraft_limit, 0.05)

        # Act
        actual_service_charge = chequing_account.get_service_charges()

        # Assert
        self.assertEqual(0.50, actual_service_charge)

    def test_str_returns_appropriate_formatted_value(self):
        """Test Case 8: Verifies the __str__ output matches the required format."""
        # Arrange
        chequing_account = ChequingAccount(1234567, 101, 1559.49, date(2023, 1, 1), 
                                           -15.0, 0.05)
        expected_output = (
            "Account Number: 1234567 Balance: $1,559.49\n"
            "Overdraft Limit: $-15.00 Overdraft Rate: 5.00% Account Type: Chequing"
        )

        # Act
        actual_output = str(chequing_account)

        # Assert
        self.assertEqual(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()