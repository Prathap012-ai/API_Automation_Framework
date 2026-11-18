import pytest

# 1. Fixture using yield
@pytest.fixture()
def employee_setup():
    print("\nEmployee setup started")
    yield
    print("\nEmployee teardown completed")


# 2. Fixture with parameters
@pytest.fixture(params=["Prathap", "Rahul", "Krishna"])
def employee_data(request):
    return request.param


# 3. Fixture dependency
@pytest.fixture()
def employee_details(employee_data):
    return {"name": employee_data}


# 4. Skip test
@pytest.mark.skip(reason="Employee feature is temporarily unavailable")
def test_skip():
    assert True


# 5. Skipif test
@pytest.mark.skipif(True, reason="Employee records are unavailable")
def test_skipif():
    assert True


# 6. XFAIL test
@pytest.mark.xfail(reason="Employee validation feature is not implemented")
def test_employee_validation():
    assert False


# 7. Employee details validation
def test_employee_details(employee_setup, employee_details):
    employee_name = employee_details["name"]
    assert employee_name in ["Prathap", "Rahul", "Krishna"]
    print(f"Employee name validated successfully: {employee_name}")