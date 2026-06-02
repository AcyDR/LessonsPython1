from selenium.webdriver.chrome.options import  Options # для вне визуального запуска
from selenium import webdriver
import pytest

@pytest.fixture
def driver(): # предусловие
    options = Options() # для вне визуального запуска
    options.add_argument('--headless') # для вне визуального запуска
    driver = webdriver.Chrome(options=options) #открывает браузер и использует опции при запуске
    driver.maximize_window() #открытие окна на весь экран
    driver.implicitly_wait(3) #ожидание
    yield driver
    driver.close()
