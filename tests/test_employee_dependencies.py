import pytest



@pytest.mark.dependency()
def test_create_employee():
    print("Employee created successfully")

@pytest.mark.dependency(depends=["test_create_employee"])
def test_update_employee():
    print("Employee updated successfully")

@pytest.mark.dependency(depends=["test_create_employee","test_update_employee"])
def test_delete_employee():
    print("Employee deleted successfully")
