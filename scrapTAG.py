import sys
import urllib.request
from bs4 import BeautifulSoup

url = sys.argv[1]

file = open("ptags.txt","w+")

soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
scrap = soup.findAll('a',{'class':'pull-left btn btn-search-pill'})

for tag in scrap:
    tags = (tag.get_text(strip=True))
    print (tags)
    file.write(tags + '\n')

file.close()
