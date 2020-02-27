import urllib.request
from bs4 import BeautifulSoup

# company = input('Ticker: ').upper()

# fp = urllib.request.urlopen('https://finance.yahoo.com/quote/'+company)
# website_bytes = fp.read()
# text = website_bytes.decode("utf-8")
# fp.close()


soup = BeautifulSoup("<p>Hello</p>")
# market_cap = soup.findAll(".Trsdu(0.3s)")


print(soup) 