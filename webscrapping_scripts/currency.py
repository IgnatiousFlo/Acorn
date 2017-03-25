"""This script scrapes the value of the pound
and the value of the Euro from a website,
then gives a conversion rate"""

from urllib import urlopen
from bs4 import BeautifulSoup


def currency_con():
    url = 'http://www.lse.co.uk/currency-converter.asp'
    pagesource = urlopen(url)
    currency_soup = BeautifulSoup(pagesource, 'html.parser')
    currency_text = currency_soup.select('1.16 EUR')
    print (currency_text)


if __name__ == '__main__':
    currency_con()

#  this gives an empty list and I don't know why.
