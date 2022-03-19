import urllib.request
from bs4 import BeautifulSoup
from collections import Counter


def find_most_frequent_words():
    soup = BeautifulSoup(urllib.request.urlopen(
        "http://www.lib.ru/EKZUPERY/mprinc.txt").read(), 'html.parser')
    s = soup.get_text()
    s = s[s.find('II'):s.find('III')]
    print(s)

    counter = Counter([''.join(filter(str.isalpha, x.lower()))
                      for x in s.split() if ''.join(filter(str.isalpha, x.lower()))])
    return(counter.most_common()[:10])

if __name__ == '__main__':
    print(find_most_frequent_words())