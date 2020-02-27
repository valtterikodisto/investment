import urllib.request
from bs4 import BeautifulSoup

def fetch_market_cap_html(company):
  fp = urllib.request.urlopen('https://finance.yahoo.com/quote/'+company)
  website_bytes = fp.read()
  text = website_bytes.decode("utf-8")
  fp.close()
  return text

def fetch_cash_flow_html(company):
  fp = urllib.request.urlopen("https://finance.yahoo.com/quote/" + company + "/cash-flow")
  website_bytes = fp.read()
  text = website_bytes.decode("utf-8")
  fp.close()
  return text

def convert_market_cap_to_number(market_cap):
  multiplier = {"M": 1000000, "B": 1000000000, "T": 1000000000000}
  
  try:
    length = len(market_cap)
    market_cap = float(market_cap[:length-1]) * multiplier.get(market_cap[length-1])
    return market_cap
  except:
    return -1

company = input('Ticker: ').upper()

market_cap_html = fetch_market_cap_html(company)
cash_flow_html = fetch_cash_flow_html(company)


soup = BeautifulSoup(market_cap_html, 'html.parser')
market_cap = soup.find("td", {"data-test": "MARKET_CAP-value"}).text
market_cap = convert_market_cap_to_number(market_cap)

soup = BeautifulSoup(cash_flow_html, 'html.parser')
cash_flow_row = soup.find('div', text="Free Cash Flow").parent.parent
free_cash_flow = -1

for i, child in enumerate(cash_flow_row.children):
  if i == 1:
    
    free_cash_flow = float("".join(child.text.split(","))) * 1000

#print("fcf " + str(free_cash_flow))
#print("mc " + str(market_cap))


if (free_cash_flow != -1 and market_cap != -1):
  ten_cap = round(free_cash_flow / market_cap * 100, 3)
  print("Ten cap: " + str(ten_cap) + "%")
else:
  print(company + " is not good")
