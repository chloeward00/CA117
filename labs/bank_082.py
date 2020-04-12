
class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename='', surname='', balance=0, account_number=0):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def __str__(self):
        name = 'Name: {} {}'.format(self.forename, self.surname)
        accountno = 'Account number: {}'.format(self.account_number)
        balances = 'Balance: {:.2f}'.format(self.balance)
        return '{}\n{}\n{}'.format(name, accountno, balances)

    def lodge(self, money):
        self.balance += money
        BankAccount.total_lodgements += 1
        return self

    def __iadd__(self, money):
        self.balance += money
        BankAccount.total_lodgements += 1
        return self

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        return self
