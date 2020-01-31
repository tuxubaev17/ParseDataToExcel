from selenium import webdriver
import time

link = 'https://chocofood.kz'
chromedriver = '/Users/alikhantuxubayev/Desktop/task/chromedriver'


browser = webdriver.Chrome(chromedriver)
browser.get(link)
browser.implicitly_wait(5)
address = 'улица Байзакова 280'
address_field = browser.find_element_by_class_name('address-field__input').send_keys(address)
button = browser.find_element_by_class_name('submit-button').click()
browser.implicitly_wait(5)
info = browser.find_element_by_css_selector(".rl-list__items .rl-list__items__item__name").text
print(info)
time.sleep(5)
browser.quit()