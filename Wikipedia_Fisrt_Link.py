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
        paragraphs = main_content.findAll('p')

        # Filter paragraphs that don't contain a span with a title attribute and exclude infobox paragraphs

        selected_paragraphs = []
        for p in paragraphs:
            if not p.get('class') == ['mw-empty-elt']: selected_paragraphs.append(p)





        #filters links for exclusions, things like citations, IPA links, etc. add to this when you encounter errors
        def filter_links(links):
            selected_links = []
            for l in links:
                if (l.get('href', '').startswith('/wiki/') and
                        not (l.get('href', '').startswith('/wiki/Help:IPA') or 
                            l.get('href', '').startswith('/wiki/File:')
                        )): selected_links.append(l)

            return selected_links


        #gets list of filtered links from 1st paragraph, chooses the 1st one as our "first link" if 1st paragraph has no links, chooses the next paragraph
        def select_first_link():
            valid_links = []
            i = 0
            while len(valid_links) == 0:
                valid_links = filter_links(selected_paragraphs[i].findAll('a'))
                i += 1

            first_link = valid_links[0]

            return first_link
        
        first_link = select_first_link()


        
        print(soup.find('title').text)
        #print(first_link)


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