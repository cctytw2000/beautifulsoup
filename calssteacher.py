import codecs    # 文字語系編碼套件
import pyquery
import requests
import urllib.parse as UP

def main():
    # 執行搜尋
    response = requests.get('https://www.google.com.tw/search?q=%s' % (UP.quote('蔡英文')))
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
            # 當標題為空時，可能是中間插入的廣告、地圖等非搜尋結果的資料
            if title.text() == '':
                continue           # data = item('div.s cite')
            # print(data.text())
            # print('')
            link = title('a')
            href = link.attr('href')
            # print(href)
            # 解析標題連結
            parse = UP.urlparse(href)
            # 讀取連結內的 QueryString
            # print(parse.query)
            # 將 QueryString 內的每組 Key=Value 分割取出
            parts = parse.query.split('&')
            for part in parts:
                # 將 Key=Value 分割取出
                pair = part.split('=')
                # print('%s: %s' % (pair[0], pair[1]))
                k = pair[0]
                v = pair[1]
                # 網站的連結存放在 k 是 q 的這組 Key=Value
                if k == 'q':
                    # 解析網站的連結
                    parse = UP.urlparse(v)
                    # 如果網站的連結沒有 scheme 的部分，代表不是有效連結，應略過該筆搜尋紀錄
                    if parse.scheme == '':
                        break
                    print(UP.unquote(title.text()))
                    print(v)
                    # TODO: 開始真正進行寫入資料庫或是資料儲存區的工作
            # 輸出一個空行以分隔每筆搜尋結果的輸出
            print('')
    else:
        print('搜尋結果回傳代碼並非 200')

if __name__ == '__main__':
    main()
