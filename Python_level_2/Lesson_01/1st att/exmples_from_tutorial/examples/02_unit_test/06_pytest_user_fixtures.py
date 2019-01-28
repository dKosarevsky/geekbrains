
# ------ Тестирование кода. Библиотека PyTest. Пользовательские фикстуры -----

# Выполните код командой в консоли:  python pytest -s <имя_данного_файла>

import pytest
 
# Простая пользовательская фикстура - это функция с декоратором @pytest.fixture()
@pytest.fixture()
def resource_setup(request):
    print("Подготовка ресурсов")

    def resource_teardown():                    # <- Функция сброса окружения
        print("Освобождение ресурсов")
    request.addfinalizer(resource_teardown)     # <- Добавление финализатора

    
# По умолчанию, scope = "function", autouse=False
@pytest.fixture(scope="function", autouse=True)
def another_resource_setup_with_autouse(request):
    print("another_resource_setup_with_autouse")
    def resource_teardown():
        print("another_resource_teardown_with_autouse")
    request.addfinalizer(resource_teardown)

# Фикстура может возвращать что-то в тест (объект/ресурс)
@pytest.fixture(scope="module")
def resource_setup(request):
    print("\n >> 'Подключение' к БД")
    db = {"Red":1, "Blue":2, "Green":3}
    def resource_teardown():
        print("\n >> 'Отключение' от БД")
    request.addfinalizer(resource_teardown)
    return db
    

@pytest.yield_fixture()
def resource_setup_with_yield():
    print("resource_setup_with_yield")
    yield
    print("resource_teardown_with_yield")


def test_1_that_needs_resource(resource_setup):
    print("test_1 - требуются ресурсы")
 

def test_2_that_does_not():
    print("test_2 - не требуются ресурсы")
 
            
@pytest.mark.usefixtures("resource_setup")
def test_3_that_does_again():
    print("test_3_that_does_again")

# Использование фикстуры с yield
def test_4_needs_resources(resource_setup_with_yield):
    print("test_4_needs_resources")

# Тесты, показывающие работу с возвращаемым из фикстуры объектом    
def test_db(resource_setup):
    for k in resource_setup.keys():
        print("Color {} has id {}".format(k, resource_setup[k]))
 
def test_red(resource_setup):
    assert resource_setup["Red"] == 1
 
def test_blue(resource_setup):
    assert resource_setup["Blue"] != 1