from selenium import webdriver
import time

def test_find_elements():
    try:
        browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements_by_xpath('//input')
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла
