class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.salary = salary


# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
print('Salary:', emp.salary)

# encapsulamento, o que passar e o que receber de dado
