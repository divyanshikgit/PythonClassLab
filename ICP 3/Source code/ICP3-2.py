
import requests
from bs4 import BeautifulSoup           # importing Beautiful soup

Link = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
Bsoup = BeautifulSoup(Link.text,"html.parser")

print(Bsoup.title.string)               # Printing the title of the address

outfile = open('output.txt','a+', encoding='utf-8')        # The output file is output.txt

for atag in Bsoup.find_all('a'):            # Iterating over each tag
    if atag.get('href'):
        outfile.write(str(atag.get('href'))+'\n')
        print(atag.get('href'))