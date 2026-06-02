from itertools import count

from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver #

    def open(self):
        self.driver.get('https://demoblaze.com/index.html')  # переход на нужную страницу браузера c помощью команды get

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH,'//a[text() = "Samsung galaxy s6"]')  # поиск елемента на странице (данные можно взять из devTool) и создание в переменную galaxy_s6 поиск по ссылке и тексту в ней XPATH
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_product_count(self):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count  # с помощью функции len узнаем количество элементов в списке monitors, а len(monitors) ==2 проверяет что, количество мониторов равно двум