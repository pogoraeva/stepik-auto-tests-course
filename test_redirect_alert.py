from selenium import webdriver
import time
import math

def test_redirect_alert():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
        link = "http://suninjuly.github.io/redirect_accept.html"
        browser.get(link)

        button = browser.find_element_by_xpath("//*[@class='trollface btn btn-primary']")
        button.click()
        time.sleep(1)
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        x_element = browser.find_element_by_xpath("/html/body/form/div/div/div/label/span[2]")
        x = x_element.text
        log = str(math.log(abs(12 * math.sin(int(x)))))
        answer = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(log)

        button = browser.find_element_by_xpath('//button[@type="submit"]')
        button.click()

    finally:
        time.sleep(15)
        browser.quit()