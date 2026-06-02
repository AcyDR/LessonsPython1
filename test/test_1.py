import pytest

@pytest.fixture() #декоратор помогает функции ниже использоваться как предусловие (фикстура)
def before_after():
    print('Before test') #предусловие
    yield None # место для запуска теста
    print('\nAfter test') # постусловие

def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 2