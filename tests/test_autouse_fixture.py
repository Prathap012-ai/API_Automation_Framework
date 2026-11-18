import pytest
@pytest.fixture(autouse=True)
def employee_setup():
    print("Employee setup started...")
    yield
    print("Employee setup completed...")

def test_employee_name():
    pass
def test_employee_department():
    pass
def test_employee_id():
    pass


