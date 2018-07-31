import codecs
import pyquery
import requests
import urllib.parse as UP


def main():
    while 1:
        word = input("請輸入你要搜尋的關鍵字:")
        response = requests.get(
            'https://www.google.com/search?q=%s' % (UP.quote(word)))
        # 判斷 HTTP 回傳代碼是 200 OK
        if response.status_code == 200:
            # 開啟 UTF-8 編碼的文字檔
            f = codecs.open('test.txt', 'w', encoding='utf-8')
            f.write(response.text)
            f.close()
        # 將下載回來的原始碼轉成 PyQuery 的文件實體
            d = pyquery.PyQuery(response.text)
        # 搜尋 class="g" 的 div（因為它是包含整筆搜尋結果的節點）
            results = d('div.g')
        # items() 可用來把 PyQuery 取回的搜尋結果輸出成 list，方便我們 for...in 取出
            for item in results.items():
                # 讀取全部
                # print(item)
                # 讀取標題
                title = item('h3.r')
                if title.text() == '':
                    continue
                # print(title.text())
            # 讀取連結
                # data = item('div.s cite')
            #     print(data.text())
            # # 輸出一個空行以分隔每筆搜尋結果的輸出
            #     print('')
                link = title('a')
                href = link.attr('href')
                parse = UP.urlparse(href)
                parts = parse.query.split('&')
                for part in parts:
                    pair = part.split('=')
                    k = pair[0]
                    v = pair[1]
                    if k == 'q':
                        parse = UP.urlparse(v)
                        if parse.scheme == '':
                            break
                        print(UP.unquote(title.text()))
                        print(v)
                print('')

        else:
            print('錯誤')


if __name__ == '__main__':
    main()
