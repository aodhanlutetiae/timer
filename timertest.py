import requests
from bs4 import BeautifulSoup as bs
url = 'https://www.theguardian.com/uk'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0'}
req = requests.get(url, headers = headers)
soup = bs(req.content)
for x in soup.find('a', class_ = 'u-faux-block-link__overlay js-headline-text'):
    headline = x
    print(headline)
