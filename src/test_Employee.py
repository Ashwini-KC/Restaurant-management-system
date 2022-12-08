import pytest
from src import Employee
@pytest.fixture
def test_employee_details():
    Employee = ('WS12','HARRY STYLES','WAITER')
    employee_details = "yuri"