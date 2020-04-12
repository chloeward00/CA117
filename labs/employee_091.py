class Employee(object):

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return "Name: {}\nNumber: {}\nWages: {:.2f}".format(self.name, self.number, self.wages())

    def wages(self):
        return 0

class Manager(Employee):

    def __init__(self, name, number, salary):
        super().__init__(name, number)
        self.salary = salary

    def wages(self):
        return self.salary / 52

class AssemblyWorker(Employee):
    def __init__(self, name, number, hourpay, hours):
        super().__init__(name, number)
        self.hourpay = hourpay
        self.hours = hours

    def wages(self):
        return self.hours * self.hourpay
