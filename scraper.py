import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    if title == title.text:
        print(title.text)

    else:
            print(title.figure)
        
    #Get all the links
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        if link['href'].find("/wiki") == -1:
            continue

        #link to scrape
        linkToScrape = link
        break

    print(linkToScrape)

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")