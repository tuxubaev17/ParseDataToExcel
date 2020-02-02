from selenium import webdriver
import time
import pandas as pd
import xlsxwriter

link = 'https://chocofood.kz'
chromedriver = '/Users/alikhantuxubayev/Documents/ChocoParser/chromedriver'
browser = webdriver.Chrome(chromedriver)


def open_browser(url):
    browser.get(url)
    browser.implicitly_wait(5)


def parse(data):
    SCROLL_PAUSE_TIME = 10
    open_browser(link)
    address = 'улица Байзакова 280'
    address_field = browser.find_element_by_class_name('address-field__input').send_keys(address)
    button = browser.find_element_by_class_name('submit-button').click()
    browser.implicitly_wait(10)
    names = browser.find_elements_by_css_selector(".rl-list__items__item__name")
    for elm in names:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        data.append(elm.text)
        print(elm.text)

    time.sleep(20)
    browser.quit()


def export_data(data):
    df = pd.DataFrame({'name': data})
    writer = pd.ExcelWriter('name.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()


data = []
parse(data)
export_data(data)
