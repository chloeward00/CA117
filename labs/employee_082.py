
class Employee(object):

    next_employee_number = 0

    def __init__(self, name='', employee_number=0, hourly_rate=9.25, hours_worked=0):
        self.name = name
        self.employee_number = Employee.next_employee_number
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        Employee.next_employee_number += 1

    def add_hours(self, hours):
        self.hours_worked += hours
        return self

    def __str__(self):
       name = 'Name: {}'.format(self.name)
       i_d = 'ID: {}'.format(self.employee_number)
       hours = 'Hours: {:.2f}'.format(self.hours_worked)
       payrate = 'Rate: {:.2f}'.format(self.hourly_rate)
       wages = 'Wages: {:.2f}'.format(self.hours_worked * self.hourly_rate)
       return '{}\n{}\n{}\n{}\n{}'.format(name, i_d, hours, payrate, wages)
