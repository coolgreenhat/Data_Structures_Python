"""
2.5 Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.

2.6 If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.

2.7 The CreditCard class of Section 2.3 initializes the balance of a new account to zero.
Modify that class so that a new account can be given a nonzero balance using an optional
fifth parameter to the constructor. The four-parameter constructor syntax should continue
to produce an account with zero balance.

2.8 Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?
"""
class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance

        The initial balance is zero.
        customer: the name of the customer
        bank: the name of the bank
        acnt: the account identifier
        limit: credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        if balance:
            self._balance = balance
        else:
            self._balance = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return name of the customer"""
        return self._bank

    def get_account(self):
        """Return the card identifying number"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return Current balance"""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit. Return True if charge was processed; False if charge was denied."""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """ Process customer payment that reduces balance."""
        if not isinstance(amount,(int)):
            raise TypeError('Please type amount as a number')
        elif amount < 0:
            raise ValueError("Amount Cannot be negative")
        self._balance -= amount



if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings','5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal','3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance','5391 0375 9387 5309', 5000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ',wallet[c].get_account())
        print('Limit = ',wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(137)
            print('New Balance = ',wallet[c].get_balance())
        print()