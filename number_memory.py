from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

AMOUNT_POINTS = 15

def main():
    wordlist = []
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('https://www.humanbenchmark.com/tests/number-memory')
    print('Log in now and return to the number memory test page. Press ENTER to continue')
    input()

    start_button = driver.find_element_by_css_selector('.hero-button')
    start_button.click()
    for i in range(AMOUNT_POINTS):
        time.sleep(0.1)
        number = driver.find_element_by_css_selector('.big-number').text
        time.sleep( ( 800*(i+1) + 1000 ) * 0.001 )
        driver.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/form/div[2]/input').send_keys(number)
        driver.find_element_by_css_selector('.hero-button').click()
        time.sleep(0.1)
        driver.find_element_by_css_selector('.hero-button').click()

if __name__ == "__main__":
    main()
    input('Press any key to exit')
