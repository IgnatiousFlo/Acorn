"""
This function shows the numbers of signatures on a petition to have a 2nd EU referendum
then gives the percentage of votes and of the populatin as a whole that have signed.
The source for the number of registered voters is:
http://www.independent.co.uk/news/uk/politics/eu-referendum-turnout-vote-polling-britain-
future-live-brexit-remain-leave-a7095146.html
Also, from the more recent trump petition https://petition.parliament.uk/petitions/171928
"""

from urllib import urlopen
from bs4 import BeautifulSoup


def percentage_func_brexit():
    url = 'https://petition.parliament.uk/petitions/131215'
    pagesource = urlopen(url).read()
    petitionsoup = BeautifulSoup(pagesource, 'html.parser')
    signitures = petitionsoup.select('.signature-count-number')
    stripped_sig = signitures[0].text.strip().split(' ')
    formatted_sig = stripped_sig[0].replace(',', '')
    print ('Brexit'), (formatted_sig)
    sig_float = float(formatted_sig)

    population = 65107000
    voters = 46499537

    voters_percent = round(sig_float/voters*100, 2)
    print (str(voters_percent) + '%')

    pop_percent = round(sig_float/population*100, 2)
    print (str(pop_percent) + '%')

if __name__ == '__main__':
    percentage_func_brexit()

print ('')

def percentage_func_trump():
    url = 'https://petition.parliament.uk/petitions/171928'
    pagesource = urlopen(url).read()
    petitionsoup = BeautifulSoup(pagesource, 'html.parser')
    signitures = petitionsoup.select('.signature-count-number')
    stripped_sig = signitures[0].text.strip().split(' ')
    formatted_sig = stripped_sig[0].replace(',', '')
    print ('Trump'), (formatted_sig)
    sig_float = float(formatted_sig)

    population = 65107000
    voters = 46499537

    voters_percent = round(sig_float/voters*100, 2)
    print (str(voters_percent) + '%')

    pop_percent = round(sig_float/population*100, 2)
    print (str(pop_percent) + '%')

if __name__ == '__main__':
    percentage_func_trump()




