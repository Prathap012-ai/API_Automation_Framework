import pytest


@pytest.mark.xfail(reason = "Known bug in employee age validation")
def test_employee_age():
    age = 15
    assert age >= 18
@pytest.mark.xfail(reason = "Department validation bug expected")
def test_employee_department():
    department = "QA"
    assert department == "QA"

@pytest.mark.xfail(strict=True,reason = "Employee ID validation bug expected")
def test_employee_id():
    employee_id = 101
    assert employee_id == 101

