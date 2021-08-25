from selenium import webdriver
import time

import math

def test_execute_script():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
        link = "http://suninjuly.github.io/execute_script.html"
        browser.get(link)

        x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
        x = x_element.text
        log = str(math.log(abs(12 * math.sin(int(x)))))
        answer=browser.find_element_by_xpath('//*[@id="answer"]').send_keys(log)

        option1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
        option1.click()

        button = browser.find_element_by_xpath('//button[@type="submit"]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)

        option2 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
        option2.click()

        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
