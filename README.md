# project-5
<img width="2400" height="640" alt="image" src="https://github.com/user-attachments/assets/05844af5-919d-4970-ac55-09b079205482" />




A tiny company that lives in your terminal. Hire a Person, promote an Employee, appoint a Manager, and watch the OOP principles do the heavy lifting.



##  Table of Contents
The Idea
Meet the Cast
OOP Concepts Cheat Sheet
How the Menu Works
See It in Action
Getting Started
Project Structure
Assumptions
Author

## The Idea

The goal of this project is to build an Employee Management System that puts core Object-Oriented Programming concepts to work: classes, inheritance, encapsulation, method overloading, method overriding and more. The system models employee data, supports adding people and viewing their details, and tracks roles such as Manager and Developer.

## Meet the Cast 

Every class has a personality:

	
1)Person :	The Blueprint	/ The base of everything: holds name and age
2)Employee:	The Worker	/ Adds a private employee_id and salary, guarded by getters and setters
3)Manager :	The Leader	/ Inherits from Employee, adds a department, and overrides display()
4)Developer:	The Builder /	Inherits from Employee, adds a programming_language, and overrides display()

<img width="1800" height="1200" alt="image" src="https://github.com/user-attachments/assets/8eaedaa1-1b37-4238-97e3-46f3cdea2107" />



## OOP Concepts Cheat Sheet ##

Concept                      | 	Where you will find it
Classes & Objects	           |  Person, Employee, Manager, Developer
Inheritance                  | 	Employee extends Person; Manager and Developer extend Employee
Encapsulation	               |  salary and employee_id are private, reached only through getters and setters
Constructor & DestructoR     |	__init__ builds objects, __del__ cleans up resources on exit
self	                       |  Refers to the current instance's attributes
Method Overriding            |	display() is customized in Manager and Developer
Method Overloading           |	Several ways to create an Employee (default and optional arguments, since Python has no                                                                                                           native overloading)
super()	                     | Reuses parent class constructors and methods
issubclass()                 |	Confirms a class belongs to the Employee family



## A quick taste of the idea (simplified sketch):
class Employee(Person):
    def __init__(self, name, age, employee_id, salary=0.0):
        super().__init__(name, age)      # reuse the parent
        self.__employee_id = employee_id # private on purpose
        self.__salary = salary

class Manager(Employee):
    def display(self):                   # override
        super().display()
        print(f"Department: {self.department}")

print(issubclass(Manager, Employee))     # True





## Full sample session:
<img width="1640" height="940" alt="image" src="https://github.com/user-attachments/assets/de24c32e-5630-49a9-8021-7f2da4bfd485" />


text
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 2
Enter Name: Jane Smith
Enter Age: 28
Enter Employee ID: E123
Enter Salary: 50000

Employee created with name: Jane Smith, age: 28, ID: E123, and salary: $50000.0.

Enter your choice: 4
Choose details to show:
1. Person
2. Employee
3. Manager
Enter your choice: 2

Employee Details:
Name: Jane Smith
Age: 28
Employee ID: E123
Salary: $50000.0

Enter your choice: 5
Exiting the system. All resources have been freed.

Goodbye!
Getting Started

Requirements: Python 3.8 or higher. No external libraries needed.

bash
# 1. Clone the repository
git clone <your-repository-url>
cd <repository-folder>

# 2. Run the program
python main.py

Replace main.py with the name of your main file if it differs.

Project Structure
text
.
├── assets/
│   ├── banner.svg
│   ├── class-diagram.svg
│   └── terminal-demo.svg
├── main.py          # classes + menu-driven interface
└── README.md
Assumptions
Person is the base class (name, age); Employee adds employee_id and salary.
Salary is stored as a float and displayed with a $ symbol.
Employee IDs are alphanumeric strings such as E123 or M456.
Python has no true method overloading, so multiple constructor styles use default arguments.
Invalid menu choices prompt the user to try again.

## Author

Tejani Janvi 

All code and content in this project are original work, created in line with the assignment's no-copying policy.

<div align="center">

Made with Python and a lot of super().

</div>


