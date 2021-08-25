import math

from selenium import webdriver
import time

def test_lesson6_step4():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
        link = "http://suninjuly.github.io/find_link_text"
        browser.get(link)
        math_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
        click_link = browser.find_element_by_partial_link_text(math_text)
        click_link.click()

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("form-control.city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_xpath('//*[@class="btn btn-default"]')
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

#не забываем оставить пустую строку в конце файла
