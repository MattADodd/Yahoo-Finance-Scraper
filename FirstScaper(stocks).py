import requests
from bs4 import BeautifulSoup

#Takes front page of Yahoo Finance stock gainers and prints their company name, company symbol, stock price change, and the change as a %
url = "https://ca.finance.yahoo.com/gainers/"
headers = {"User-Agent": "Matt"}
stocks = requests.get(url, headers=headers)
soup = BeautifulSoup(stocks.text, "html.parser")
info = soup.find_all("div", class_ = "Pos(r) Pos(r) Mih(265px)")
for stock in info:
    changes = stock.find_all("fin-streamer", class_ = "Fw(600)")
    company_name = stock.find_all("td", class_ ="Va(m) Ta(start) Px(10px) Fz(s)")
    symbol = stock.find_all("a", class_ ="Fw(600) C($linkColor)")
all_info = zip(company_name, symbol, changes[0::2], changes[1::2])
for com_name, sym, chan, chanp in all_info:
    print(f"""Company: {com_name.text}
Symbol: {sym.text}
Change: {chan.text}
% Change: {chanp.text} 
""")


