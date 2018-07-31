import selenium.webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as BY
from selenium.webdriver.support import ui as UI
from selenium.webdriver.support import expected_conditions as EC
word = input('請輸入你要搜尋的關鍵字:')


def main():
    option = selenium.webdriver.ChromeOptions()
    driver = selenium.webdriver.Chrome(chrome_options=option)
    driver.get('https://www.google.com.tw/')
    # search = driver.find_element_by_css_selector('input#lst-ib')
    search = UI.WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((BY.CSS_SELECTOR, 'input#lst-ib'))
    )

    search.clear
    search.send_keys(word)
    search.send_keys(Keys.RETURN)
    button = driver.find_element_by_css_selector('input[name="btnI"]')
    # print(button.get_attribute('value'))
    time.sleep(600)


if __name__ == '__main__':
    main()
