# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Nishant Malhotra

## Assignment

Assignment 1: In this assignment you will leverage the knowledge gained in Module 01 to develop classes to support a larger system. This is the first of many assignments in this course, each of which will build on the previous assignment in order to produce a complete system. The focus of this assignment aligns with the focus of the first module - that is, classes, encapsulation and unit test planning.

Assignment 2: This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

## Encapsulation

Polymorphism is a fancy word for a simple idea. 
Different objects can respond to the same command in their own way. Even though they all have the same name,
they act differently depending on which account you are using.
This program treats every account as just a "BankAccount", 
and tells each one to calculate its charges by calling get_service_charges().
Chequing account checks if the balance is below overdraft limit and adds a
fee if it is.
Savings account looks to see if the balance is below the minimum and doubles 
the charge if it is.
Investment account checks the date the account was opened.
If its over 10 years old, it waives the fee entirely.
