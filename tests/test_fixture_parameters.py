import pytest

@pytest.fixture(params=["Prathap","Rahul","Krishna"])
def employee_data(request):
    return request.param

def test_employee_name(employee_data):
    assert employee_data in ["Prathap","Rahul","Krishna"]

