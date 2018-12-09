from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

AMOUNT_POINTS = 420

def main():
    wordlist = []
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.humanbenchmark.com/tests/verbal-memory')
    print('Log in now and return to the verbal memory test page. Press ENTER to continue')
    input()

    start_button = driver.find_element_by_css_selector('.button.start')
    start_button.click()
    for i in range(AMOUNT_POINTS):
        time.sleep(0.01)
        word = driver.find_element_by_css_selector('.word.ng-scope').text
        if word not in wordlist:
            wordlist.append(word)
            print(f'{i+1}: NEW {word}')
            driver.find_element_by_link_text('NEW').click()
        else:
            print(f'{i+1}: {word}')
            driver.find_element_by_link_text('SEEN').click()
    print(f'Total amount of words remembered: {len(wordlist)}')

if __name__ == "__main__":
    main()
    input('')