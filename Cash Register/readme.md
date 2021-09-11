# Cash Register Proof of Concept

This is an example of a cash register program in Python.

## Description

This is a basic cash register program. Functionality exists to add or remove items from a cart. Items may have set quantities and prices.
Additional manager settings allow for overriding prices, applying discounts, changing the set tax rate, and shutting down the register.
Upon checkout a receipt will be generated in the root folder. 
Any actions performed in the manager console will be logged to a separate file with the ID of the manager.


## Getting Started

Enter the name of an item to begin. Prompts for quantity and price will follow. 

### Dependencies

* datetime
* sys

### Installing

No installation is necessary, but the first time the program is run it will download a city list sized approximately 40MB.

### Executing program

* Pressing enter on a blank line will show the contents of the cart

* Entering - into the prompt will enter the Item removal menu

* Entering + into the prompt will enter the Item addition menu

* Entering * into the prompt will enter the manager console, giving extra options

* Enter 'checkout' to complete the checkout process



## Author

[Matthew Fikes](https://www.linkedin.com/in/matthew-fikes-0ab91213/)

