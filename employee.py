class Employee:
    def _init_(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def _init_(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        return [employee for employee in self.employees if employee.age == target_age]

    def search_by_name(self, target_name):
        return [employee for employee in self.employees if employee.name.lower() == target_name.lower()]

    def search_by_salary(self, operator, target_salary):
        if operator == ">":
            return [employee for employee in self.employees if employee.salary > target_salary]
        elif operator == "<":
            return [employee for employee in self.employees if employee.salary < target_salary]
        elif operator == ">=":
            return [employee for employee in self.employees if employee.salary >= target_salary]
        elif operator == "<=":
            return [employee for employee in self.employees if employee.salary <= target_salary]
        else:
            return []

def main():
    database = EmployeeDatabase()

    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search options:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter age : "))
        result = database.search_by_age(age)
    elif choice == 2:
        name = input("Enter name : ")
        result = database.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (>, <, <=, >=): ")
        salary = int(input("Enter salary: "))
        result = database.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    if result:
        print("Search Results:")
        for employee in result:
            print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No results found.")

if __name__ == "_main_":
    main()
#