'''
    Программа для авторизации в ФБ через Google Chrome
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sleeptime = 3

# опции хрома
# ----------------------------------------------------------------------------------------
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
# ----------------------------------------------------------------------------------------
# запуск хрома
driver = webdriver.Chrome(chrome_options=option)
# переход на сайт
driver.get('https://facebook.com')

# ввод логина пароля, клик по кнопке
driver.find_element_by_xpath('''//*[@id="email"]''').send_keys(input('Введите логин: '))  # логин
time.sleep(sleeptime)
driver.find_element_by_xpath('''//*[@id="pass"]''').send_keys(input('Введите пароль: '))  # пароль
time.sleep(sleeptime)
driver.find_element_by_xpath('''//*[@id="u_0_b"]''').click()  # клик по кнопке
time.sleep(sleeptime)

# переход на страницу с настройками
driver.get('https://www.facebook.com/settings?tab=account&section=email&view')
time.sleep(sleeptime)
# переход на фрейм
frame = driver.find_element_by_xpath('''//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/iframe''')
time.sleep(sleeptime)
driver.switch_to.frame(frame)
time.sleep(sleeptime)

# переход на форму ввода пароля
driver.find_element_by_xpath('''//a[text()='+ Добавить другой электронный адрес или номер мобильного телефона']''').click()
time.sleep(sleeptime * 2)

# ввод нового адреса
driver.find_element_by_name('new_email').send_keys('mysin_id@mail.ru')
time.sleep(sleeptime)
driver.find_element_by_xpath('''//button[text()='Добавить']''').click()
time.sleep(sleeptime)
driver.find_element_by_xpath('''//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div[3]/a''').click()  # закрыть
time.sleep(sleeptime)
driver.find_element_by_xpath('''//a[text()='Подтвердить']''').click()
