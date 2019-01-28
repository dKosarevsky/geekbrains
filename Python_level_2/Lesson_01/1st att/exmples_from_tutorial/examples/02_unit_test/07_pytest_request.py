
# ------ Тестирование кода. Библиотека PyTest. Объект request -----------

# Выполните код командой в консоли:  python pytest -s <имя_данного_файла>

import pytest
 
# Вывод некоторых атрибутов объекта request 
@pytest.fixture(scope="function")
def resource_setup(request):
    print()
    print ('01', request.fixturename)
    print ('02', request.scope)
    print ('03', request.function.__name__)
    print ('04', request.cls)
    print ('05', request.module.__name__)
    print ('06', request.fspath)
    
def test_1(resource_setup):
    assert True
 
class TestClass():
    def test_2(self, resource_setup):
        assert True
