from selenium import webdriver
import time
from PIL import Image

# Создание экземпляра браузера
driver = webdriver.Chrome()

# Переход на нужную веб-страницу
driver.get('https://www.msn.com/ru-xl/weather/forecast/in-%D0%9A%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D0%BA,%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C?loc=eyJsIjoi0JrQvtC%2F0LXQudGB0LoiLCJyIjoi0KfQtdC70Y%2FQsdC40L3RgdC60LDRjyDQvtCx0LvQsNGB0YLRjCIsInIyIjoi0JrQvtC%2F0LXMgdC50YHQutC40Lkg0LPQvtGA0L7QtNGB0LrQvsyB0Lkg0L7MgdC60YDRg9CzIiwiYyI6ItCg0L7RgdGB0LjRjyIsImkiOiJSVSIsImciOiJydS14bCIsIngiOiI2MS42MjgyMzEwNDg1ODM5ODQiLCJ5IjoiNTUuMTE3MjIxODMyMjc1MzkifQ%3D%3D&weadegreetype=C')

# Ожидание загрузки страницы
time.sleep(1)

# Получение высоты страницы
height = driver.execute_script("return document.body.scrollHeight")

# Установка размера окна браузера для прокрутки
driver.set_window_size(1920, height)

# Прокрутка страницы до конца
for i in range(1, height, 500):
    driver.execute_script(f'window.scrollTo(0, {i});')
    time.sleep(0.1)

time.sleep(5)

# Создание скриншота всей страницы
driver.save_screenshot('screenshot5.png')

# Закрытие браузера
driver.quit()