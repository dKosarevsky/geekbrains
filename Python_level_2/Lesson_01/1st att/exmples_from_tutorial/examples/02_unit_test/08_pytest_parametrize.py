
# ------ Тестирование кода. Библиотека PyTest. Параметризация ----------------

# Выполните код командой в консоли:  python pytest -s <имя_данного_файла>

import pytest
 
def strange_string_func(s):
    ''' 'Подопытная' функция для тестов
    '''
    if len(s) > 5:
        return s + "?"
    elif len(s) < 5:
        return s + "!"
    else:
        return s + "."
 

@pytest.fixture(scope="function", params=[
    ("abcdefg", "abcdefg?"),
    ("abc", "abc!"),
    ("abcde", "abcde.")
])
def param_test(request):
    return request.param


def test_strange_string_func(param_test):
    in_str, expected_output = param_test
    result = strange_string_func(in_str)
    print("\ninput: {0}, output: {1}, expected: {2}".format(in_str, result, expected_output))
    assert result == expected_output

    
@pytest.mark.parametrize("x", [1,2])
@pytest.mark.parametrize("y", [10,11])
def test_cross_params(x, y):
    print("x: {0}, y: {1}".format(x, y))
    assert True
