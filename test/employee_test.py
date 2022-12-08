from src import Employee
from util import create_random_id
import string
from random_id import *

empID = create_random_id()

def test_add_employee():
    empName = "John Doe"
    empType = 2

    emp = Employee()
    print(emp.add_employee(empID, empName, empType), "Added")

def test_employee_details():
    emp = Employee()
    print(emp.employee_details(empID))

def test_delete_employee():
    emp = Employee()
    print(emp.delete_employee(empID), "Deleted")

def test_update_employee():
    emp = Employee()
    print(emp.update_employee(empID, {"empName": "Jane Doe"}), "Updated")

def test_get_all_employees():
    emp = Employee()
    all_emp = emp.get_all_employees()
    for employee in all_emp:
        print(employee)