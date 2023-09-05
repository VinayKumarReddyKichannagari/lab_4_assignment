class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmpTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, operator, target_age):
        result = []
        for emp in self.employees:
            if operator == '>' and emp.age > target_age:
                result.append(emp)
            elif operator == '<' and emp.age < target_age:
                result.append(emp)
            elif operator == '>=' and emp.age >= target_age:
                result.append(emp)
            elif operator == '<=' and emp.age <= target_age:
                result.append(emp)
        return result

    def search_by_name(self, target_name):
        result = []
        for emp in self.employees:
            if emp.name.lower() == target_name.lower():
                result.append(emp)
        return result

    def search_by_salary(self, operator, target_salary):
        result = []
        for emp in self.employees:
            if operator == '>' and emp.salary > target_salary:
                result.append(emp)
            elif operator == '<' and emp.salary < target_salary:
                result.append(emp)
            elif operator == '>=' and emp.salary >= target_salary:
                result.append(emp)
            elif operator == '<=' and emp.salary <= target_salary:
                result.append(emp)
        return result

    def display_employee_data(self, emp_list):
        if len(emp_list) == 0:
            print("No matching records found.")
        else:
            for emp in emp_list:
                print("\nEmployee ID:", emp.emp_id)
                print("Name:", emp.name)
                print("Age:", emp.age)
                print("Salary:", emp.salary)

def main():
    emp_table = EmpTable()
    
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("\nMenu:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            operator = input("Enter the age operator (>, <, >=, <=): ")
            target_age = int(input("Enter the age to search for: "))
            result = emp_table.search_by_age(operator, target_age)
        elif choice == '2':
            target_name = input("Enter the name to search for: ")
            result = emp_table.search_by_name(target_name)
        elif choice == '3':
            operator = input("Enter the salary operator (>, <, >=, <=): ")
            target_salary = float(input("Enter the salary value: "))
            result = emp_table.search_by_salary(operator, target_salary)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        emp_table.display_employee_data(result)

main()
