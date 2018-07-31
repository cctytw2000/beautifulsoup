import codecs    # 文字語系編碼套件
import pyquery
import requests
import urllib.parse as UP
import time

def main():
    
    response = requests.get('http://www.books.com.tw/web/books_nbtopm_19/')
    
    if response.status_code == 200:
      
        f = codecs.open('book.txt', 'w', encoding='utf-8')
        f.write(response.text)
        f.close()
       
        d = pyquery.PyQuery(response.text)
        
        results = d('div.item')
        
        for item in results.items():
           
            title = item('div.msg h4')
            print(title)
            href = item('a').attr('href')
            print(href)
            author = item('div.msg>ul>li').text()
            print(author)
            price = item('div.price_box li.set1').text()
            print(price)
          
        print('')
    else:
        print('搜尋結果回傳代碼並非 200')

    time.sleep(2)

if __name__ == '__main__':
    main()