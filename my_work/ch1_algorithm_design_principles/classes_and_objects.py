class Employee:
    numEmployee = 0

    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1

    def __repr__(self):
        return "a custom object (%r)" % self.name

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, num_hours):
        self.owed += num_hours * self.rate
        return "%.2f hours worked" % num_hours

    def pay(self):
        self.owed = 0
        return "payed %s" % self.name


# inheritance
class SpecialEmployee(Employee):
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate)
        self.bonus = bonus

    def hours(self, num_hours):
        self.owed += num_hours * self.rate + self.bonus
        return "%.2f hours worked" % num_hours


# class methods
# class Aexp:
#     base = 2
#
#     @classmethod
#     def exp(cls, x):
#         return cls.base ** x
#
#
# class Bexp(Aexp):
#     __base = 3
#
#     def __exp(self):
#         return x ** cls.base


# emp1 = Employee("Anna", 8.50)
# emp2 = Employee("Mark", 12.34)
#
# print(emp1.hours(20), emp1.owed, emp1.pay())
# print(emp2)
