import requests
from bs4 import BeautifulSoup
import html5lib

def myspider(max_pages):
    page = 1
    while page < max_pages:
        url = "http://www.umairsalam.com/blog/?paged=" + str(page)
        source_code = requests.get(url)                                 # get raw text from the web url
        plain_text = source_code.text                                   # convert to plain text
        soup = BeautifulSoup(plain_text, 'html5lib')                    # beautiful soup html5 text
        just_links = soup.find_all('h1', class_="entry-title p-name")  # find_all method to locate h1
        page += 1
#        print(just_links)
#        print(type(just_links))
        return just_links




links_text = myspider(2)
print(links_text)