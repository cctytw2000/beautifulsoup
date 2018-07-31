import codecs
import pyquery
import requests
import time
import urllib.parse as UP
def money (left):
    for money in left.items() :
           return money.items()


def main():
    # 載入博客來的網站
    response = requests.get('http://www.books.com.tw/web/books_nbtopm_19/')
    # 判斷 HTTP 回傳代碼是 200 OK
    if response.status_code == 200:
        # 開啟 UTF-8 編碼的文字檔
        f = codecs.open('book.html', 'w', encoding='utf-8')
        f.write(response.text)
        f.close()
        # 將下載回來的原始碼轉成 PyQuery 的文件實體
        d = pyquery.PyQuery(response.text)
        #
        posts = d('div.msg')
        # left = d('ul.price li.set1')
        for post in posts.items():           
            #取得書籍的網址
            link = post('a').attr('href')
            print('書籍連結:'+link)
            #取得 名子
            title = post('h4').text()
            print('書籍名稱:'+title)
            #取得 作者
            worker = post('li.info a').text()
            print('書籍作者:'+worker)
            # 用呼叫def取得價格
            left = d('div.price_box li.set1')
            print('書籍價格:'+left.text())

            # 輸出一個空行以分隔每筆搜尋結果的輸出
            print('')
            # 每次存取間隔一秒
            time.sleep(2)
    else:
        print('搜尋結果回傳代碼並非 200')

if __name__ == '__main__':
    main()
