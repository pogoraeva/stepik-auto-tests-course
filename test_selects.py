
from selenium import webdriver
import time
import math


def test_selects():
    browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    summary = str(int(num1)+int(num2))
    print(summary)

    browser.find_element_by_id("dropdown").click()
    time.sleep(2)

    browser.find_element_by_xpath(f"//*[contains(text(), {summary})]").click()
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
    time.sleep(10)
