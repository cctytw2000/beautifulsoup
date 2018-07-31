import requests
import bs4

def main():
    response = requests.get('https://tw.appledaily.com/new/realtime')
    d = bs4.BeautifulSoup(response.text, 'html.parser')
    p = d.find('li', 'rtddt')
    print(p.get_text())

if __name__ == '__main__':
    main()