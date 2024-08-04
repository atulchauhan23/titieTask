import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qUrl = 'https://books.toscrape.com/'

qHeader = {
    'user- agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

qResp = rq.get(url = qUrl,headers = qHeader)

bSoup = BeautifulSoup(qResp.content, 'html.parser')

def removeNavigableString(value):
    return list(filter(lambda x : type(x) != NavigableString, value))

c1 =removeNavigableString(bSoup.ol.children)

# print(c1[0].h3.getText())

title = [ol.h3.getText() for ol in c1]
print(title)

# c11 = c1[4].h3.a.attrs['title']
# print(c11)

# c12 = c1[5].h3.a.attrs['title']
# print(c12)