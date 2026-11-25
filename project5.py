
# ==========================================
# PYTHON OOP PROJECT
# EMPLOYEE MANAGEMENT SYSTEM
# ==========================================

# ---------- PERSON CLASS ----------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)


# ---------- EMPLOYEE CLASS ----------
class Employee(Person):

    def __init__(self, name, age, employee_id="Not Assigned", salary=0):
        super().__init__(name, age)

        self.__employee_id = employee_id
        self.__salary = float(salary)

    # Getter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for Employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for Salary
    def get_salary(self):
        return self.__salary

    # Setter for Salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = float(salary)
        else:
            print("Salary cannot be negative!")

    # Method Overriding
    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())

    # Destructor
    def __del__(self):
        pass


# ---------- MANAGER CLASS ----------
class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Department:", self.department)


# ---------- DEVELOPER CLASS ----------
class Developer(Employee):

    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Programming Language:", self.programming_language)


# ---------- MAIN PROGRAM ----------

people = []
employees = []
managers = []
developers = []

print("--- Python OOP Project: Employee Management System ---")

while True:

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # CREATE PERSON
    if choice == "1":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)
        people.append(person)

        print("\nPerson created with name:",
              name, "and age:", age)

    # CREATE EMPLOYEE
    elif choice == "2":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)
        employees.append(employee)

        print("\nEmployee created with name:", name,
              ", age:", age,
              ", ID:", emp_id,
              "and salary: $", employee.get_salary())

    # CREATE MANAGER
    elif choice == "3":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)
        managers.append(manager)

        print("\nManager created with name:", name,
              ", age:", age,
              ", ID:", emp_id,
              ", salary: $", manager.get_salary(),
              "and department:", department)

    # SHOW DETAILS
    elif choice == "4":

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")

        detail_choice = input("Enter your choice: ")

        if detail_choice == "1":
            if people:
                for p in people:
                    p.display()
            else:
                print("No Person records found.")

        elif detail_choice == "2":
            if employees:
                for e in employees:
                    e.display()
            else:
                print("No Employee records found.")

        elif detail_choice == "3":
            if managers:
                for m in managers:
                    m.display()
            else:
                print("No Manager records found.")

        elif detail_choice == "4":
            if developers:
                for d in developers:
                    d.display()
            else:
                print("No Developer records found.")

        else:
            print("Invalid choice!")

    # EXIT
    elif choice == "5":

        print("\nExiting the system. All resources have been freed.")
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")


# ---------- CHECKING INHERITANCE ----------
print("\nInheritance Verification:")
print("Is Manager a subclass of Employee?",
      issubclass(Manager, Employee))

print("Is Developer a subclass of Employee?",
      issubclass(Developer, Employee))
