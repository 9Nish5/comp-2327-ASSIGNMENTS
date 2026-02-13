import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    """Unit tests for the SavingsAccount class."""

    def test_init_valid_attributes_set_correctly(self):
        # 1. Arrange - Test Case 1
        account_number = 456
        client_number = 1010
        balance = 100.0
        date_created = date(2024, 1, 1)
        minimum_balance = 50.0

        # 2. Act
        savings_account = SavingsAccount(account_number, client_number, balance, 
                                         date_created, minimum_balance)

        # 3. Assert
        self.assertEqual(account_number, savings_account._BankAccount__account_number)
        self.assertEqual(minimum_balance, savings_account._SavingsAccount__minimum_balance)

    def test_init_invalid_minimum_balance_type_sets_default(self):
        # 1. Arrange - Test Case 2
        invalid_minimum = "invalid_type"
        expected_default = 50.0

        # 2. Act
        savings_account = SavingsAccount(456, 1010, 100.0, date.today(), invalid_minimum)

        # 3. Assert
        self.assertEqual(expected_default, savings_account._SavingsAccount__minimum_balance)

    def test_get_service_charges_balance_greater_than_minimum(self):
        # 1. Arrange - Test Case 3
        # Balance $100.0 is greater than Minimum $50.0
        savings_account = SavingsAccount(456, 1010, 100.0, date.today(), 50.0)
        expected_charge = 0.50

        # 2. Act
        actual_charge = savings_account.get_service_charges()

        # 3. Assert
        self.assertEqual(expected_charge, actual_charge)

    def test_get_service_charges_balance_equal_to_minimum(self):
        # 1. Arrange - Test Case 4
        # Balance $50.0 is equal to Minimum $50.0
        savings_account = SavingsAccount(456, 1010, 50.0, date.today(), 50.0)
        expected_charge = 0.50

        # 2. Act
        actual_charge = savings_account.get_service_charges()

        # 3. Assert
        self.assertEqual(expected_charge, actual_charge)

    def test_get_service_charges_balance_less_than_minimum(self):
        # 1. Arrange - Test Case 5
        # Balance $25.0 is less than Minimum $50.0 (Charge should double)
        savings_account = SavingsAccount(456, 1010, 25.0, date.today(), 50.0)
        expected_charge = 1.00

        # 2. Act
        actual_charge = savings_account.get_service_charges()

        # 3. Assert
        self.assertEqual(expected_charge, actual_charge)

    def test_str_returns_appropriate_formatted_value(self):
        # 1. Arrange - Test Case 6
        savings_account = SavingsAccount(456, 1010, 100.0, date(2024, 1, 1), 50.0)
        expected_output = ("Account Number: 456 Balance: $100.00\n"
                           "Minimum Balance: $50.00 Account Type: Savings")

        # 2. Act
        actual_output = str(savings_account)

        # 3. Assert
        self.assertEqual(expected_output, actual_output)