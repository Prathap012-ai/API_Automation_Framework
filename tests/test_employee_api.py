import pytest


@pytest.mark.smoke
def test_get_employee_details(api):
    response = api.get("/users/1")
    assert response.status_code == 200
    response_body = response.json()
    print(response_body)
    employee_name = response_body["name"]
    employee_email = response_body["email"]
    employee_city = response_body["address"]["city"]

    assert  employee_name == "Leanne Graham",f"Expected name 'Leanne Graham' but got {employee_name}"
    assert employee_email == "Sincere@april.biz",f"Expected email 'Sincere@april.biz' but got {employee_email}"
    assert employee_city == "Gwenborough", f"Expected city 'Gwenborough' but got {employee_city}"

@pytest.mark.smoke
def test_create_employee(api):
    employee = {
        "name": "Prathap",
        "username": "prathap_qa",
        "email": "prathap@example.com"
    }
    response = api.post('/users',employee)
    assert response.status_code == 201
    response_body = response.json()
    name = response_body["name"]
    username = response_body["username"]
    email = response_body["email"]

    assert  name == "Prathap",f"Expected name 'Prathap' but got {name}"
    assert username == "prathap_qa",f"Expected username 'prathap_qa' but got {username}"
    assert email == "prathap@example.com", f"Expected email 'prathap@example.com' but got {email}"

@pytest.mark.regression
def test_update_employee(api):
    employee = {
        "name": "Prathap updated",
        "username": "prathap_qa_updated",
        "email": "prathap.updated@example.com"
    }
    response = api.put('/users/1',employee)
    assert response.status_code == 200
    response_body = response.json()
    name = response_body["name"]
    username = response_body["username"]
    email = response_body["email"]

    assert  name == "Prathap updated",f"Expected name 'Prathap updated' but got {name}"
    assert username == "prathap_qa_updated",f"Expected username 'prathap_qa updated' but got {username}"
    assert email == "prathap.updated@example.com", f"Expected email 'prathap.updated@example.com' but got {email}"

@pytest.mark.regression
def test_delete_employee(api):
    response = api.delete("/users/1")
    assert response.status_code == 200
    print("Response status code: ", response.status_code)

@pytest.mark.parametrize("user_id,expected_name,expected_city",[(1,"Leanne Graham","Gwenborough"),(2,"Ervin Howell","Wisokyburgh"),(3,"Clementine Bauch","McKenziehaven")],)
def test_get_multiple_employee_details(api,user_id,expected_name,expected_city):
    response = api.get(f"/users/{user_id}")
    assert response.status_code == 200
    response_body = response.json()
    name = response_body["name"]
    city = response_body["address"]["city"]
    assert name == expected_name, f"Expected name '{expected_name}' but got {name}"
    assert city == expected_city, f"Expected city '{expected_city}' but got {city}"


@pytest.mark.parametrize("user_id",[0,9999],)
def test_get_employee_not_found(api,user_id):
    response = api.get(f"/users/{user_id}")
    assert response.status_code == 404,f"Expected status code '404' but invalid user ID {user_id},but got response{response.status_code}"





