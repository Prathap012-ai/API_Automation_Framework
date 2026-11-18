import pytest


@pytest.mark.order(1)
def test_create_employee():
    print("create employee")

@pytest.mark.order(2)
def test_update_employee():
    print("update employee")

@pytest.mark.order(3)
def test_delete_employee():
    print("delete employee")
