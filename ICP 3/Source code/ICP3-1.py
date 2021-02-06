class Employee:             # Create a class Employee
    employeeCnt = 0
    totalsal = 0            # var for total salary
    average = 0             # var for calculating average

    def __init__(self, name, surname,salary, department):      # defining with init and self
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department
        Employee.averageSal(salary)

    def averageSal(salary):         # defining the average salary
        Employee.employeeCnt += 1
        Employee.totalsal += salary
        Employee.average = Employee.totalsal / Employee.employeeCnt


class permanentEmployee(Employee):          # Created class for permanent employee
    def __init__(self, name, surname, salary, department):
        Employee.__init__(self, name, surname, salary, department)


emp = Employee("Alexx", "Al", 1, "CS")
emp = Employee("Kothari","Div", 2, "CSEE")
permanent = permanentEmployee("Divyanshi","Kothari",3,"ECE")
emp = Employee("Alex","Vel", 4, "IT")
print("The permanent Employee is",permanent.name)               # To print the permanent employee
print("Average Salary of the employee is",Employee.average)     # To print the average salary
print("Total Employee in numbers is",Employee.employeeCnt)      # To print the total employee