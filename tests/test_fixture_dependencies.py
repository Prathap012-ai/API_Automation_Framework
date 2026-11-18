import pytest


@pytest.fixture
def employee_data():
    return {
    "id": 101,
    "name": "Prathap",
    "department": "QA"
}
@pytest.fixture()
def employee_details(employee_data):
    emp_name = employee_data["name"]
    emp_dept = employee_data["department"]

    return f"Employee Name:{emp_name}, Department:{emp_dept}"

def test_employee_details(employee_details,employee_data):
    assert "Prathap" in employee_details,f"Expected emp_name 'Prathap',but got {employee_details}"
    assert "QA" in employee_details,f"Expected emp_department 'QA',but got {employee_details}"
    assert employee_data["name"] == "Prathap",f"Expected emp_name 'Prathap',but got {employee_data['name']}"
    assert employee_data["department"] == "QA",f"Expected emp_department 'QA',but got {employee_data['department']}"


