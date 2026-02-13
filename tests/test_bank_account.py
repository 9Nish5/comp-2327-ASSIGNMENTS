"""Unit testing for the BankAccount class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """
    Unit tests for the BankAccount class.
    Requirements: Use name mangling for private attributes and round floats to 2 decimal places.
    """

    def test_init_valid_data_sets_attributes(self):
        """Test Case 1: Valid inputs correctly set the private attributes."""
        # Arrange & Act
        account = BankAccount(20019, 1010, 500.0)
        
        # Assert using name mangling (_ClassName__attribute)
        self.assertEqual(20019, account._BankAccount__account_number)
        self.assertEqual(1010, account._BankAccount__client_number)
        self.assertEqual(500.0, account._BankAccount__balance)

    def test_init_invalid_balance_sets_zero(self):
        """Test Case 2: Non-numeric balance defaults to 0.0."""
        account = BankAccount(20019, 1010, "invalid_balance")
        self.assertEqual(0.0, account._BankAccount__balance)

    def test_init_invalid_account_number_raises_exception(self):
        """Test Case 3: Non-integer account number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            BankAccount("ABC", 1010, 500.0)
        self.assertEqual("Account number must be an integer.", str(context.exception))

    def test_update_balance_positive_amount(self):
        """Test Case 8: update_balance adds a positive value."""
        account = BankAccount(20019, 1010, 500.0)
        account.update_balance(100.0)
        self.assertEqual(600.0, account._BankAccount__balance)

    def test_update_balance_negative_amount(self):
        """Test Case 9: update_balance adds a negative value (subtraction)."""
        account = BankAccount(20019, 1010, 500.0)
        account.update_balance(-100.0)
        self.assertEqual(400.0, account._BankAccount__balance)

    def test_update_balance_invalid_amount_no_change(self):
        """Test Case 10: Non-numeric amount does not change balance."""
        account = BankAccount(20019, 1010, 500.0)
        account.update_balance("invalid")
        self.assertEqual(500.0, account._BankAccount__balance)

    def test_deposit_valid_amount(self):
        """Test Case 11: deposit updates balance correctly."""
        account = BankAccount(20019, 1010, 500.0)
        account.deposit(100.0)
        self.assertEqual(600.0, account._BankAccount__balance)

    def test_deposit_negative_amount_raises_exception(self):
        """Test Case 12: Negative deposit raises ValueError with currency formatting."""
        account = BankAccount(20019, 1010, 500.0)
        with self.assertRaises(ValueError) as context:
            account.deposit(-50.0)
        # Requirement: Deposit amount: {formatted amount} must be positive.
        self.assertEqual("Deposit amount: -$50.00 must be positive.", str(context.exception))

    def test_withdraw_valid_amount(self):
        """Test Case 13: withdraw updates balance correctly."""
        account = BankAccount(20019, 1010, 500.0)
        account.withdraw(100.0)
        # Requirement: Use round() for float precision
        self.assertEqual(400.0, round(account._BankAccount__balance, 2))

    def test_withdraw_negative_amount_raises_exception(self):
        """Test Case 14: Negative withdraw raises ValueError."""
        account = BankAccount(20019, 1010, 500.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(-50.0)
        self.assertEqual("Withdraw amount: -$50.00 must be positive.", str(context.exception))

    def test_withdraw_exceeds_balance_raises_exception(self):
        """Test Case 15: Withdraw more than balance raises ValueError with formatting."""
        account = BankAccount(20019, 1010, 100.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(500.0)
        
        # Requirement: Withdraw amount: {formatted amount} must not exceed the account balance: {formatted balance}.
        expected_msg = "Withdraw amount: $500.00 must not exceed the account balance: $100.00."
        self.assertEqual(expected_msg, str(context.exception))

    def test_str_representation(self):
        """Test Case 16: Returns string in expected format with currency and newline."""
        account = BankAccount(20019, 1010, 6764.67)
        # Requirement: Account Number: {val} Balance: ${val} followed by a line feed (\n)
        expected = "Account Number: 20019 Balance: $6,764.67\n"
        self.assertEqual(str(account), expected)

if __name__ == '__main__':
    unittest.main()


