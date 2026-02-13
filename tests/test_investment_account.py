import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def test_init_valid_attributes_set_correctly(self):
        # 1. Arrange
        account_number = 789
        client_number = 1010
        balance = 1000.0
        date_created = date(2020, 1, 1)
        management_fee = 2.50

        # 2. Act
        account = InvestmentAccount(account_number, client_number, balance, 
                                    date_created, management_fee)

        # 3. Assert
        self.assertEqual(account_number, account._BankAccount__account_number)
        self.assertEqual(management_fee, account._InvestmentAccount__management_fee)

    def test_init_invalid_management_fee_sets_default(self):
        # 1. Arrange
        invalid_fee = "invalid"

        # 2. Act
        account = InvestmentAccount(789, 1010, 1000.0, date.today(), invalid_fee)

        # 3. Assert
        self.assertEqual(2.55, account._InvestmentAccount__management_fee)

    def test_get_service_charges_under_ten_years_applies_fee(self):
        # 1. Arrange (Account created 5 years ago)
        date_created = date.today() - timedelta(days=5 * 365.25)
        account = InvestmentAccount(789, 1010, 1000.0, date_created, 2.50)
        expected = 0.50 + 2.50  # Base + Fee

        # 2. Act
        actual = account.get_service_charges()

        # 3. Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_exactly_ten_years_waives_fee(self):
        # 1. Arrange (Account created exactly 10 years ago)
        date_created = date.today() - timedelta(days=10 * 365.25)
        account = InvestmentAccount(789, 1010, 1000.0, date_created, 2.50)
        expected = 0.50  # Fee waived

        # 2. Act
        actual = account.get_service_charges()

        # 3. Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_over_ten_years_waives_fee(self):
        # 1. Arrange (Account created 11 years ago)
        date_created = date.today() - timedelta(days=11 * 365.25)
        account = InvestmentAccount(789, 1010, 1000.0, date_created, 2.50)
        expected = 0.50

        # 2. Act
        actual = account.get_service_charges()

        # 3. Assert
        self.assertEqual(expected, actual)

    def test_str_within_ten_years_shows_fee_amount(self):
        # 1. Arrange
        date_created = date.today()
        account = InvestmentAccount(789, 1010, 1000.0, date_created, 2.50)
        expected_part = "Management Fee: $2.50"

        # 2. Act
        actual_str = str(account)

        # 3. Assert
        self.assertIn(expected_part, actual_str)

    def test_str_over_ten_years_shows_waived(self):
        # 1. Arrange
        date_created = date.today() - timedelta(days=11 * 365.25)
        account = InvestmentAccount(789, 1010, 1000.0, date_created, 2.50)
        expected_part = "Management Fee: Waived"

        # 2. Act
        actual_str = str(account)

        # 3. Assert
        self.assertIn(expected_part, actual_str)