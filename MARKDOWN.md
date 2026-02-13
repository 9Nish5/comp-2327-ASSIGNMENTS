1. Can I explain what my code does?
 My code implements a hierarchical banking system using OOP in Python. 
 It features a BankAccount superclass that handles common data like 
 account number and balances.
 There are three specific account types:
    - ChequingAccount: Manages overdraft limits and applies fees if the balance drops too low.

    - InvestmentAccount: Includes logic to waive management fees for clients, 
                         who have had their accounts for 10 years or more than 10 years.

    - SavingAccount: Enforces a minimum balance, doubling the service charge if the balance falls
                     below the threshold.

2. What was my coding process?
 - Planning: After carefully reviewing the assignment,
             I followed the instructions and did the whole project as it was instructed.

 - Implementation: I built each subclass individually, 
                   ensuring they properly inherited from the BankAccount parent class.

 - Verification: I used the Arrange-Act-Assert pattern to write unit tests for every method. 
                 I ran these tests frequently to catch errors early.

 - Demonstration: Finally, I implemented the A02_main.py script to simulate real-world usage,
                  such as deposits, withdrawals, and automated month-end fee processing.

3. What challenges did I have?
 The most significant challenge was mastering String Formatting and Name Mangling.

 - The Challenge: During unit testing for the __str__ method, my tests initially failed due to
                  invisible characters, such as extra newlines or misplaced spaces in the f-strings.
 - The solution: I had to carefully run back-to-back tests and look at the error codes, 
                 for any hint I could find to fix my output. After I fixed it in the first Subclass,
                 the rest were easy work for me.

4. What would I do differently now?
 I would definitely plan ahead for the tests and fill in the test excel sheets before so that I do not
 waste my time looking at the code again and again to fill out the sheets.