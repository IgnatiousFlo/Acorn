"""
Sunrise scrapper. gives the sunrise time for Oxford each day.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime


def sunrise():
    # Make the soup
    url = "https://www.timeanddate.com/sun/uk/oxford"
    page_source = urlopen(url).read()
    the_soup = BeautifulSoup(page_source, 'html.parser')

    # find the heading
    print(the_soup.findAll("h2")[1])

    #
    print(the_soup.find("data-day=\"13\""))

    now = datetime.datetime.now()
    print(now.strftime("%d"))

"""
for td in the_soup:
    if tr data day == today:
        print(time)
"""



if __name__ == '__main__':
    sunrise()