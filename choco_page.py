from selenium import webdriver
import time
import pandas as pd
import xlsxwriter

link = 'https://chocofood.kz'
chromedriver = 'path to chromedriver'
browser = webdriver.Chrome(chromedriver)


def write_data():
    df = pd.DataFrame({'name': data})
    writer = pd.ExcelWriter('name.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()


def open(url):
    browser.get(url)
    browser.implicitly_wait(5)


def steps(data):
    open(link)
    address = 'улица Байзакова 280'
    address_field = browser.find_element_by_class_name('address-field__input').send_keys(address)
    button = browser.find_element_by_class_name('submit-button').click()
    browser.implicitly_wait(15)

    names = browser.find_elements_by_css_selector(".rl-list__items__item__name")
    for elm in names:
        data.append(elm.text)
        print(elm.text)

    time.sleep(15)
    browser.quit()
    write_data()


data = []
steps(data)
