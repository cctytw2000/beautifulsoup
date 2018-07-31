import selenium.webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as BY
from selenium.webdriver.support import ui as UI
from selenium.webdriver.support import expected_conditions as EC
# email = input("請輸入帳號")
# password= input("請輸入密碼:")
def main():
    f = open('password.txt' , 'r')
    pwd = f.read()
    f.close()


    option = selenium.webdriver.ChromeOptions()
    driver = selenium.webdriver.Chrome(chrome_options=option)
    driver.get('https://www.facebook.com/')
    # search = driver.find_element_by_css_selector('input#lst-ib')
    facebookemail = UI.WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((BY.CSS_SELECTOR, 'input#email'))
    )
    facebookpassword = UI.WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((BY.CSS_SELECTOR, 'input#pass'))
    )

    facebookemail.send_keys('cctytw2000@yahoo.com.tw')
    facebookpassword.send_keys(pwd)
    facebookpassword.submit()
    name = UI.WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((BY.CSS_SELECTOR, 'a[title^="葉冠麟"]'))
    )
    print('以載入個人動態牆')
    driver.get('https://www.facebook.com/tsaiingwen/')
    funs = UI.WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((BY.CSS_SELECTOR, 'h1#seo_h1_tag'))
    )
    print('以載入總統動態')
    # talk = driver.find_element_by_css_selector('div.userContent _3576 p')
    # print(talk.text())
    posts =  UI.WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((BY.CSS_SELECTOR, 'div.userContentWrapper'))
    )  
    for post in posts:
        usercontent = post.find_element_by_css_selector('div.userContent')
        # print(word.text)
        paragraphs = usercontent.find_elements_by_css_selector('p')
        content = ''
        for paragraph in paragraphs:
                content = content + paragraph.text + '\n'
        print(content)
        print('')
    


    time.sleep(600)


if __name__ == '__main__':
    main()
