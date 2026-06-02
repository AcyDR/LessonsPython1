from selenium import webdriver
import pytest

@pytest.fixture
def driver(): # предусловие
    driver = webdriver.Chrome() #открывает браузер
    driver.maximize_window() #открытие окна на весь экран
    driver.implicitly_wait(3) #ожидание
    yield driver
    driver.close()