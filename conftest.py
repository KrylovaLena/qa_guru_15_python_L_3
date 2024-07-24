import pytest
@pytest.fixture(scope="session")
def browser():
    print ("Открыть браузер!")

    yield

    print ("Закрыть браузер!")