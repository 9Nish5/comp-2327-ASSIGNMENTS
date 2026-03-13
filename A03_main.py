"""A program to demonstrate your understanding of the Observer Pattern.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nishant Malhotra"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client
from datetime import date


# 2. Create a Client object with data of your choice.
client_1 = Client(123, "Ezio", "Auditore", "ezio.auditore@ac.com")

# 3a. Create a ChequingAccount object with data of your choice, using 
#   the client_number of the client created in step 2.
chequing = ChequingAccount(1001, 123, 500.0, date.today(), -100.0, 0.05)

# 3b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in step 2.
savings = SavingsAccount(2001, 123, 1000.0, date.today(), 50.0)


# 4. The ChequingAccount and SavingsAccount objects are 'Subject' 
# objects. The Client object is an 'Observer' object.  
# 4a. Attach the Client object (created in step 1) to the 
#   ChequingAccount object (created in step 2).
chequing.attach(client_1)

# 4a. Attach the Client object (created in step 1) to the 
#   SavingsAccount object (created in step 2).
savings.attach(client_1)


# 5a. Create a second Client object with data of your choice.
client_2 = Client(456, "Tony", "Stark", "tony.stark@aven.com")

# 5b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in this step.
savings_2 = SavingsAccount(3001, 456, 200.0, date.today(), 50.0)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and 
# withdraws) which would cause the Subject (BankAccount) to notify the 
# Observer (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    print("Executing large deposit...")
    chequing.deposit(15000.0)

    print ("Executing withdrawal to low balance...")
    chequing.withdraw(15480.0)

    print("Executing standard transaction (no notification)...")
    savings.deposit(10.0)
except Exception as e:
    print(f"Transaction Error: {e}")
