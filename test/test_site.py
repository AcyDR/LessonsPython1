from selenium import webdriver #импорт селениума
from selenium.webdriver.common.by import By #импорт способов поисков по элементу
import pytest
import time

# Открытие сайта - открыть новую страницу - кликнуть по ссылке - проверка страницы на соответствие тексту
def test_open_s6(driver):
    driver.get('https://demoblaze.com/index.html') # переход на нужную страницу браузера c помощью команды get
    galaxy_s6 = driver.find_element(By.XPATH,'//a[text() = "Samsung galaxy s6"]') # поиск елемента на странице (данные можно взять из devTool) и создание в переменную galaxy_s6 поиск по ссылке и тексту в ней XPATH
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'

# Открытие сайта - из списка кликнуть на мониторы - и убедиться что на странице отображается 2 товара
def test_two_monitors(driver):
    driver.get('https://demoblaze.com/index.html')
    monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2) # желательно, не использовать для тестов ожидание по времени, лучше использовать ожидание изменения чего-то на странице, url, цвета кнопки или текста кнопки и т. д.
    monitors = driver.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) ==2 # с помощью функции len узнаем количество элементов в списке monitors, а len(monitors) ==2 проверяет что, количество мониторов равно двум