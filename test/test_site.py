from itertools import product

from selenium import webdriver #импорт селениума
from selenium.webdriver.common.by import By #импорт способов поисков по элементу
import pytest
import time
from pages.homepage import  HomePage # для того что бы использовались файлы из нашей инструкции
from pages.product import ProductPage # для того что бы использовались файлы из нашей инструкции

# Открытие сайта - открыть новую страницу - кликнуть по ссылке - проверка страницы на соответствие тексту
def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')

# Открытие сайта - из списка кликнуть на мониторы - и убедиться что на странице отображается 2 товара
def test_two_monitors(driver):
    driver.get('https://demoblaze.com/index.html')
    monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2) # желательно, не использовать для тестов ожидание по времени, лучше использовать ожидание изменения чего-то на странице, url, цвета кнопки или текста кнопки и т. д.
    monitors = driver.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) ==2 # с помощью функции len узнаем количество элементов в списке monitors, а len(monitors) ==2 проверяет что, количество мониторов равно двум