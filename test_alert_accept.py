from selenium import webdriver
import time
import math

def test_alert_accept():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
        link = "http://suninjuly.github.io/alert_accept.html"
        browser.get(link)

        button = browser.find_element_by_xpath("//*[@class='btn btn-primary']")
        button.click()
        confirm = browser.switch_to.alert
        confirm.accept()

        x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
        x = x_element.text
        log = str(math.log(abs(12 * math.sin(int(x)))))
        answer = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(log)

        button = browser.find_element_by_xpath('//button[@type="submit"]')
        button.click()

    finally:
        time.sleep(15)
        browser.quit()