import urllib.parse as UP

def main():
    url = 'https://www.google.com/search?q=%E9%A6%AC%E8%8B%B1%E4%B9%9D&ei=ZVALW6H8FonL0ATq26boCQ&start=10&sa=N&biw=1920&bih=974'
    res = UP.urlparse(url)  #分解 網址
    print(res)
    # res = res._replace(query='q=/S/DKCA18')  #改  QUERY裡面的東西
    # url = UP.urlunparse(res)
    # print(url)
    # res = res._replace(netloc='store.pchome.com.tw')  #改  netloc裡面的東西
    # url = UP.urlunparse(res)
    # print(url)

if __name__ == '__main__':
    main()