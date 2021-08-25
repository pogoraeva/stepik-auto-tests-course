from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium import webdriver
import time
import math

def test_redirect_alert():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser.get(link)

        price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        button = browser.find_element_by_id("book")
        button.click()

        x_element = browser.find_element_by_xpath("/html/body/form/div/div/div/label/span[2]")
        x = x_element.text
        log = str(math.log(abs(12 * math.sin(int(x)))))
        answer = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(log)

        button = browser.find_element_by_xpath('//button[@type="submit"]')
        button.click()

    finally:
        time.sleep(15)
        browser.quit()

