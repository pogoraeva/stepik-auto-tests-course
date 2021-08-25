from selenium import webdriver
import time

def test_file_input():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=r"O:\chromedriver\chromedriver.exe")
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)

        input1 = browser.find_element_by_name("firstname")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name("lastname")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_name("email")
        input3.send_keys("aaa")

        element = browser.find_element_by_name("file").send_keys("O://pythonProject//aaa.txt")

        button = browser.find_element_by_xpath('//button[@type="submit"]')
        button.click()

    finally:
        time.sleep(10)
        browser.quit()
