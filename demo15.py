import pyquery
import requests


def main():
    response = 'https://www.google.com/search?ei=hmwKW7L3HcyV0gSgtJa4Dw&q=%E9%A6%AC%E8%8B%B1%E4%B9%9D&oq=%E9%A6%AC%E8%8B%B1%E4%B9%9D&gs_l=psy-ab.3..0i131k1j0l9.14901.19468.0.20204.18.17.1.0.0.0.62.680.16.17.0....0...1c.1j4.64.psy-ab..0.13.537.6..0i30k1j0i5i30k1j35i39k1j0i13k1.36.qf6fpU_Ai90'
    # d = pyquery.PyQuery(response.text)
    print(response.split('&'))
    # print(d.text())
    # p = d('cite')
    # for i in p:
    # print(p.text())
    # response = requests.get('https://www.google.com.tw/')
    # print(response.text)

if __name__ == '__main__':
    main()
