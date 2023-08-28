# python file
class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

def sort_employees(employees, sort_parameter):
    if sort_parameter == 1:  # Sort by Age
        employees.sort(key=lambda emp: emp.age)
    elif sort_parameter == 2:  # Sort by Name
        employees.sort(key=lambda emp: emp.name)
    elif sort_parameter == 3:  # Sort by Salary
        employees.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]
    
    print("Select sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    sort_param = int(input())
    
    sort_employees(employees, sort_param)
    
    print("\nSorted Employee Table:")
    for emp in employees:
        print(emp)
