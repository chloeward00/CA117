class Customer(object):

    discount = 0.0

    def __init__(self, name='', balance=0, addr_line1='', addr_line2='', addr_line3=''):
        self.name = name
        self.balance = balance
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.addr_line3 = addr_line3

    def owes(self):
        return (self.balance - (self.balance * self.discount))

    def __str__(self):
        name = '{}'.format(self.name)
        address1 = '{}'.format(self.addr_line1)
        address2 = '{}'.format(self.addr_line2)
        address3 = '{}'.format(self.addr_line3)
        balance = 'Balance: {:.2f}'.format(self.balance)

        sid = self.discount * 100
        discount = 'Discount: {:.0f}%'.format(sid)

        amount = 'Amount due: {:.2f}'.format(self.owes())

        return '{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(name, address1, address2, address3, balance, discount, amount)

class ValuedCustomer(Customer):

    discount = 0.1
