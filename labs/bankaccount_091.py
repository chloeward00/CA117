class BankAccount(object):

    next_account_number = 16555232
    account_type = 'General'

    def __init__(self, forename, surname, balance):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def __str__(self):
        return "Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}".format(self.forename + " " + self.surname, self.account_number, self.account_type, self.balance)

    def lodge(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount:
            print ("Insufficient funds available")
        else:
            self.balance = self.balance - amount

class CurrentAccount(BankAccount):

    float_overdraft = -1000
    account_type = 'Current'

    def withdraw(self, amount):
        if self.balance < amount + self.float_overdraft:
            print ("Insufficient funds available")

        else:
            self.balance = self.balance - amount

    def __str__(self):
        return "Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nOverdraft: {:.2f}".format(self.forename + " " + self.surname, self.account_number, self.account_type, self.balance, self.float_overdraft)

class SavingsAccount(BankAccount):
    interest_rate = 0.01
    account_type = "Savings"

    def __str__(self):
        return "Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nInterest rate: {:.2f}".format(self.forename + " " + self.surname, self.account_number, self.account_type, self.balance, self.interest_rate)

    def apply_interest(self):
        self.balance *= 1 + SavingsAccount.interest_rate
