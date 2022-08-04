#this program will read the exported chrome bookmark file
#and get the names of every anime that's from turkanime
#and add the names to anime_names.txt with the dates

import re
import codecs

def extract_links_from_bookmarks():
    links = []
    done_seen = False
    with codecs.open("bookmarks.html", "r", encoding='utf-8') as f:
        for line in f.readlines():
            if "Done" in line:
                done_seen = True
            if "www.turkanime" in line and "/anime" in line and done_seen:
                m = re.search('HREF="(.+?)" ADD_DATE', line)
                found = m.group(1)
                links.append(found)
            if "To Watch" in line:
                done_seen = False
    return links
        
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_names_from_links(seq):
    #https://www.pythonpool.com/urllib-error-httperror-http-error-403-forbidden/
    url = "http://www.turkanime.co/anime/gungrave"
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(request_site)
    soup = BeautifulSoup(webpage, 'html.parser')
    title = soup.find('div', {"class": "panel-title"})
    print(title)
    #for link in seq:
        #url = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'})
        #try:
            #page = urlopen(url)
        #except:
            #print("Error opening the URL!")
        #soup = BeautifulSoup(page, 'html.parser')
        #title = soup.find('div', {"class": "panel-title"})
        #print(title)

    pass

get_names_from_links(extract_links_from_bookmarks())