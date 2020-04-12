class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, money):
        self.money = money
        self.balance = self.balance + self.money

    def withdraw(self, money):
        self.money = money
        self.balance = self.balance - self.money
        if self.balance < 0:
            self.balance = self.balance + self.money
            print('Insufficient funds available')

    def __str__(self):
        return('Your current balance is: {:.2f} euro'.format(self.balance))
