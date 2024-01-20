import requests
from bs4 import BeautifulSoup

# URL of the Yahoo Finance stock gainers page
url = "https://ca.finance.yahoo.com/gainers/"

# Set a custom User-Agent header to avoid any issues with web scraping
headers = {"User-Agent": "Matt"}

# Send a GET request to the specified URL with the custom headers
stocks = requests.get(url, headers=headers)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(stocks.text, "html.parser")

# Find all div elements with the specified class that contains stock information
info = soup.find_all("div", class_="Pos(r) Pos(r) Mih(265px)")

# Iterate over each stock in the retrieved information
for stock in info:
    # Find all elements with the specified class that contain stock price change information
    changes = stock.find_all("fin-streamer", class_="Fw(600)")

    # Find all elements with the specified class that contain company name information
    company_name = stock.find_all("td", class_="Va(m) Ta(start) Px(10px) Fz(s)")

    # Find all elements with the specified class that contain company symbol information
    symbol = stock.find_all("a", class_="Fw(600) C($linkColor)")

# Combine company name, symbol, change, and percentage change information using zip
all_info = zip(company_name, symbol, changes[0::2], changes[1::2])

# Iterate over the zipped information and print details for each stock
for com_name, sym, chan, chanp in all_info:
    print(f"""Company: {com_name.text}
Symbol: {sym.text}
Change: {chan.text}
% Change: {chanp.text} 
""")


