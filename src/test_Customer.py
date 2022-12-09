from src import Employee, Customer
import pytest


def test_delete_employee():
    emp = Employee()
    empID='19'
    emp1={'EmpID': "19", 'EmpName': "Hue Janas", 'EmpType': "1"}
    assert emp1== emp.delete_employee(empID)


    

 