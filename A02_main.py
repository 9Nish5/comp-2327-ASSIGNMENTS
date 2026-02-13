"""A program to demonstrate the use of the BankAccount subclasses.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nishant Malhotra"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing = ChequingAccount(1234, 101, -200.0, date.today(), -100.0, 0.05)

# 3. Print the ChequingAccount created in step 2.
print(chequing)
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing.get_service_charges():.2f}")


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing.deposit(500.0)
# 4b. Print the ChequingAccount
print(chequing)
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing.get_service_charges():.2f}")

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings = SavingsAccount(5678, 102, 500.0, date.today(), 50.0)

# 6. Print the SavingsAccount created in step 5.
print(savings)
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

print(f"Service Charges: ${savings.get_service_charges():.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings.withdraw(475.0)

# 7b. Print the SavingsAccount.
print(savings)
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings.get_service_charges():.2f}")

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_new = InvestmentAccount(9012, 103, 1000.0, date.today(), 2.50)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_new)
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(f"Service Charges: ${investment_new.get_service_charges():.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
ten_years_ago = date.today() - timedelta(days=11*365.25)
investment_old = InvestmentAccount(3456, 104, 1000.0, ten_years_ago, 2.50)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_old)
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(f"Service Charges: ${investment_old.get_service_charges():.2f}")


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
accounts = [chequing, savings, investment_new, investment_old]

for account in accounts:
    charge = account.get_service_charges()
    account.withdraw(charge)


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
for account in accounts:
    print(account)
