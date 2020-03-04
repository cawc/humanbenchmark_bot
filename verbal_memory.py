from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

AMOUNT_POINTS = 169

def main():
    wordlist = []
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('https://www.humanbenchmark.com/tests/verbal-memory')
    print('Log in now and return to the verbal memory test page. Press ENTER to continue')
    input()

    start_button = driver.find_element_by_css_selector('.hero-button')
    start_button.click()
    for i in range(AMOUNT_POINTS):
        time.sleep(0.01)
        word = driver.find_element_by_css_selector('.word').text
        if word not in wordlist:
            wordlist.append(word)
            print(f'{i+1}: NEW {word}')
            driver.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[3]/button[2]').click()
        else:
            print(f'{i+1}: {word}')
            driver.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[3]/button[1]').click()
    print(f'Total amount of words remembered: {len(wordlist)}')

if __name__ == "__main__":
    main()
    input('Press any key to exit')
