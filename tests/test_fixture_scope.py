import pytest


@pytest.fixture(scope="function")
def function_fixture():
    print("Function fixture setup")
    yield
    print("Function fixture teardown")

@pytest.fixture(scope="class")
def class_fixture():
    print("class fixture setup started..")
    yield
    print("class fixture teardown")

@pytest.fixture(scope="module")
def module_fixture():
    print("module fixture setup started")
    yield
    print("module fixture teardown")

@pytest.fixture(scope="session")
def session_fixture():
    print("session fixture setup started")
    yield
    print("session fixture teardown")


class TestFixtureScope:

    def test_one(self, function_fixture, class_fixture, module_fixture, session_fixture):
        pass

    def test_two(self, function_fixture, class_fixture, module_fixture, session_fixture):
        pass


def test_three(function_fixture, module_fixture, session_fixture):
    pass


def test_four(function_fixture, module_fixture, session_fixture):
    pass