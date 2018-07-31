import codecs
import pyquery
import requests
import time
import urllib.parse as UP

# 抓取單筆新聞
def grabPage(link, category):
    # 判斷連結是否有效
    if link is None:
        return
    print(category)
    # 下載新聞
    response = requests.get(link)
    # 判斷 HTTP 回傳代碼是 200 OK
    if response.status_code == 200:
        # 開啟 UTF-8 編碼的文字檔
        f = codecs.open('applenews.txt', 'w', encoding='utf-8')
        f.write(response.text)
        f.close()
        # 將下載回來的原始碼轉成 PyQuery 的文件實體
        d = pyquery.PyQuery(response.text)
        # 讀取新聞標題
        title = d('article.ndArticle_leftColumn h1').text()
        print(title)
        article = d('div.ndArticle_margin > p')
        paragraphs = article.text().split('\n')
        content = ''
        for paragraph in paragraphs:
            if paragraph.startswith('發稿時間'):
               break
            content = content + paragraph + '\n'
        print(content)

def main():
    # 載入即時新聞清單
    response = requests.get('https://tw.appledaily.com/new/realtime')
    # 判斷 HTTP 回傳代碼是 200 OK
    if response.status_code == 200:
        # 開啟 UTF-8 編碼的文字檔
        f = codecs.open('applenews.txt', 'w', encoding='utf-8')
        f.write(response.text)
        f.close()
        # f = open('note.html','w',encoding='utf-8')
        # f.write(response.text)
        # f.close()
        # 將下載回來的原始碼轉成 PyQuery 的文件實體
        d = pyquery.PyQuery(response.text)
        #
        posts = d('li.rtddt')
        for post in posts.items():
            # print(post)
            # 讀取新聞標題
            # title = post('h1').text()
            # print(title)
            # 讀取新聞類別
            category = post('h2').text()
            # print(category)
            # 讀取新聞連結
            link = post('a').attr('href')
            print(link)
            # 抓取單筆新聞並傳入新聞頁內缺少的類別資訊
            grabPage(link, category)
            # 輸出一個空行以分隔每筆搜尋結果的輸出
            print('')
            # 每次存取間隔一秒，避免全班同時爆量查詢而被蘋果新聞阻擋連線
            time.sleep(1)
    else:
        print('搜尋結果回傳代碼並非 200')

if __name__ == '__main__':
    main()
