from selenium import webdriver
import time

import pandas as pd
import xlsxwriter

link = 'https://chocofood.kz'
chromedriver = '/Users/alikhantuxubayev/Desktop/task/chromedriver'

browser = webdriver.Chrome(chromedriver)
browser.get(link)
browser.implicitly_wait(5)
address = 'улица Байзакова 280'
address_field = browser.find_element_by_class_name('address-field__input').send_keys(address)
button = browser.find_element_by_class_name('submit-button').click()
time.sleep(5)
name = []
s = []
s = browser.find_elements_by_css_selector(".rl-list__items__item__name")
for elm in s:
    name.append(elm.text)

time.sleep(15)
browser.quit()

df = pd.DataFrame({'Data':name})
writer = pd.ExcelWriter('name.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


