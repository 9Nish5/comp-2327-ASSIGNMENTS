# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Nishant Malhotra

## Assignment

Assignment 1: [Indicate the name and description of the current assignment]

## Encapsulation

1. Data Hiding (Private Attributes)

Encapsulation starts by hiding the internal state of the object. In the BankAccount class, attributes like balance, account_number, and client_number were defined using Double Underscores (e.g., self.__balance).

    Why: This triggers Name Mangling, making it difficult for external code to accidentally or intentionally modify the balance without going through the proper channels.

    Result: You cannot simply call account.__balance = 1000000 from your main.py.

2. Controlled Access (Properties/Getters)

To allow other parts of the program to see the data without changing it directly, Properties (Getters) were used.

    The @property decorator allows the balance to be read like a variable (print(account.balance)).

    Because no @balance.setter was created, the balance is effectively read-only from the outside.

3. Protection of Integrity (Validation Methods)

Instead of allowing direct modification of attributes, the class provides public methods like deposit() and withdraw(). These act as "gatekeepers."

    Validation: These methods check if the input is numeric, positive, or if there are sufficient funds before changing the __balance.

    Single Point of Truth: The actual update to the balance happens in a private/internal method (update_balance), ensuring that the logic for changing money is centralized and secure.
