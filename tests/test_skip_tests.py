
import pytest

@pytest.mark.skip( reason= "Employee name feature is temporarily unavailable")
def test_employee_name():
    assert True

employee_count = 0
@pytest.mark.skipif(employee_count == 0,reason="No employee records available")
def test_employee_records():
    assert employee_count ==0


def test_employee_department():
    department = "QA"
    assert department == "QA"

