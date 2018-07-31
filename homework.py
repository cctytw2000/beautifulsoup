import requests
from bs4 import BeautifulSoup
#下載
r = requests.get('https://www.google.com/search?safe=strict&ei=WZAKW5qBFcar8QXghpewBQ&q=python&oq=python&gs_l=psy-ab.3..35i39k1l2j0i67k1l8.12941.15400.0.15686.8.7.1.0.0.0.53.346.7.7.0....0...1.1.64.psy-ab..0.8.347...0j0i131k1j0i10k1.0.iuJyeduBYsk')
soup = BeautifulSoup(r.text,'html.parser')
items = soup.select('div.g > h3.r > a[href^="/url"]')

for i in items :
    print('標題:'+i.text)
    print('網址:'+i.get('href'))


    


