from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/trending-cryptocurrencies/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

coin_table = soup.findAll('tbody')

coin_table = coin_table[0]

coin_rows = coin_table.findAll('tr')

for x in coin_rows [:5]:
    td = coin_rows[x].findAll('td')
    name = td[0].text
    price = td[1].text
    oneday_percent = td[2].text
    total_gross = td[7].text

    print(name)







if bitcoin < 40000:


if Ethereum < 3000: 


input('')
