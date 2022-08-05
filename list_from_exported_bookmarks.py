#this program will read the exported chrome bookmark file
#and get the names of every anime that's from turkanime
#and add the names to anime_names.txt with the dates

import re
import codecs

def extract_links_from_bookmarks():
    links = []
    replacement = "co"
    done_seen = False
    with codecs.open("bookmarks.html", "r", encoding='utf-8') as f:
        for line in f.readlines():
            if "Done" in line:
                done_seen = True
            if "www.turkanime" in line and "/anime" in line and done_seen:
                m = re.search('HREF="(.+?)" ADD_DATE', line)
                found = m.group(1)
                #urllib struggles to open a website with websites old extension
                #even tho website reroutes to their updated site
                #upcoming code changes the extension at www.website.EXTENSION
                #between turkanime and /anime words
                reg = "(?<=%s).*?(?=%s)" % ("turkanime.","/anime")
                r = re.compile(reg, re.DOTALL)
                result = r.sub(replacement, found)
                links.append(result)
            if "To Watch" in line:
                done_seen = False
    return links
        
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_names_from_links(seq):
    #https://www.pythonpool.com/urllib-error-httperror-http-error-403-forbidden/

    #url = "http://www.turkanime.co/anime/ajin"
    #request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    #webpage = urlopen(request_site)

    #soup = BeautifulSoup(webpage, 'html.parser')
    #divTag = soup.find_all("div", {"id": "detayPaylas"})
    #for tag in divTag:
        #extracted = tag.find("div", {"class": "panel-title"})
    #n = re.search('">(.+?) <', str(extracted))
    #title = n.group(1)
    #print(title)

    names = []
    for link in seq:
        url = link
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        webpage = urlopen(request_site)

        soup = BeautifulSoup(webpage, 'html.parser')
        divTag = soup.find_all("div", {"id": "detayPaylas"})
        for tag in divTag:
            extracted = tag.find("div", {"class": "panel-title"})
        n = re.search('">(.+?) <', str(extracted))
        title = n.group(1)
        names.append(title)
    
    for item in names:
        print(item)

    pass

get_names_from_links(extract_links_from_bookmarks())