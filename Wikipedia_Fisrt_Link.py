#this works in theory but the biggest problem now is that it's going to the wikipedia main page whenever it's clicking a reference link, and then it just does down the same path everytime
#it needs to not click reference links, i.e. exclude links in brackets

import requests
from bs4 import BeautifulSoup

def article_selector(url): 

    n = 0

    while True:
        n += 1

        html = requests.get(url)

        soup = BeautifulSoup(html.content, 'html.parser')

        title_text = soup.find('title').text
        
        # Find the main content div
        main_content = soup.find(id="mw-content-text")

        # Find all paragraphs
        paragraphs = main_content.find_all('p')

        # Filter paragraphs that don't contain a span with a title attribute and exclude infobox paragraphs

        selected_paragraphs = []
        for p in paragraphs:
            if not p.get('class') == ['mw-empty-elt']: selected_paragraphs.append(p)



        #instead let's do the same thing, find all links in the first paragraph and then choose the good ones also, if there aren't any, check the next paragraph

        links = selected_paragraphs[0].findAll('a')



        #this might be better but it also needs to exclude IPA links about pronunciation, they contain 'IPA'
        print(links)
        selected_links = []
        for l in links:
            if not l.get('href', '').startswith('#cite_note-'): selected_links.append(l)


        print(selected_links)


        #link we click is the first of the links that fit our qualifications
        first_link = selected_links[0]
        
        print(soup.find('title').text)
        #print(first_link)
        #print(href)


        #print(selected_paragraphs[0].text)

        

        if title_text == 'Philosophy - Wikipedia':

            print("You made it to Philosophy!")
            print ("That took " + str(n) + " steps.")

            break


        #update the url with the first link href

        url = "https://en.wikipedia.org" + first_link.get('href')
    return

def main():
    url = 'https://en.wikipedia.org/wiki/Special:Random'

    article_selector(url)

    return

if __name__ == "__main__": main()