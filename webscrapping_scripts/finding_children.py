"""Makes a soup then from the soup take all the h2 tags, finds the child
and return the titles as strings and then same but return a list of strings.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup


def find_children():
    url = 'http://www.naomiklein.org/main'
    pagesource = urlopen(url).read()
    naomi_soup = BeautifulSoup(pagesource, 'html.parser')

    naomi_title = naomi_soup.find('title').string
    print(naomi_title)

    naomi_h2s = naomi_soup.find_all('h2')
    for h2s in naomi_h2s:
        for child in h2s.findChildren():
            print(child.text)

    titles = []
    for h2s in naomi_h2s:
        for child in h2s.findChildren():
            titles.append(child.text)
    print(titles)

if __name__ == '__main__':
    find_children()
