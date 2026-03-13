# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Nishant Malhotra

## Assignment

Assignment 1: In this assignment you will leverage the knowledge gained in Module 01 to develop classes to support a larger system. This is the first of many assignments in this course, each of which will build on the previous assignment in order to produce a complete system. The focus of this assignment aligns with the focus of the first module - that is, classes, encapsulation and unit test planning.

Assignment 2: This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

Assignment 3: This is a banking system that handles different types of accounts (Chequing, Savings, and Investment). For this assignment, I updated the code to use two important "Design Patterns" called Strategy and Observer. These help make the code cleaner and easier to change later.

## Strategy Pattern
I moved the math for calculating service charges out of the main account files and into their own "Strategy" files.

* **Why?: Instead of one giant file doing everything, the BankAccount now just asks a specific strategy object to handle 
          the math.
* **How it Works?:
        1. I removed BASE_SERVICE_CHARGE from the BankAccount class.
        2. Each account (like ChequingAccount) now has its own strategy.
        3. For example, the Overdraft Strategy calculates fees based on the overdraft limit and rate.

## The Observer Pattern
I set up a system where the BankAccount can "talk" to the Client automatically whenever something
important happens.

* **The Subject: The BankAccount is the "Subject". It keeps a list of people to notify.
* **The Observer: The Client is the "Observer". It waits for a message from the bank.
* **The Alerts: When you deposit or withdraw money, the bank checks two things:
            1. Low balance: If the balance drops below $50.0, it sends an alert.
            2. Large Transactions: If you move more than $10,000.00 at once, it sends an alert.
