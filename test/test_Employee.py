import pytest
from src import Employee

def test_add_employee():
    emp = Employee()
    emptype = '6'
    empid = '6666'
    empname = 'jjs'
    emp1 ={'empID':"6666",'empName':"jjs",'empType': "6"}
    
    assert emp1 == emp.add_employee(empid,empname,emptype)
    
def test_delete_employee():
    emp = Employee()
    empID='6666'

    emp1 = {'empID':"6666", 'empName' : "jjs" , 'empType' : '6'}
    assert emp1 == emp.delete_employee(empID)
def test_update_employee():
    emp = Employee()
    empID='6666'
    emp1 = {'empID':'66666','empName' : "jjjs" , 'empType' : '666'}
    assert emp1 == emp.update_employee(empID)
