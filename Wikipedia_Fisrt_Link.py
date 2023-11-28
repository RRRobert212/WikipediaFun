#this works in theory but the biggest problem now is that it's going to the wikipedia main page whenever it's clicking a reference link, and then it just does down the same path everytime
#it needs to not click reference links, i.e. exclude links in brackets

import requests
from bs4 import BeautifulSoup

def article_selector(url): 

    n = -1

    while True:
        n += 1

        html = requests.get(url)

        soup = BeautifulSoup(html.content, 'html.parser')



        #selects paragraphs from main text content and filters them for known exclusions
        def filter_paragraphs():

            main_content = soup.find(id="mw-content-text")   
            paragraphs = main_content.findAll('p')

            selected_paragraphs = []
            for p in paragraphs:
                if not p.get('class') == ['mw-empty-elt']: selected_paragraphs.append(p)

            return selected_paragraphs
        
        selected_paragraphs = filter_paragraphs()





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

        #make title readable
        title_text = soup.find('title').text[:-12]
        


        #check if we are at the Philosophy page, if so stop, and say how long it took to get there.
        if title_text == 'Philosophy':

            print(title_text)
            print("You made it to Philosophy!")
            print ("That took " + str(n) + " steps.")

            break


        #print the page title and update the url with our first_link
        print(title_text)
        url = "https://en.wikipedia.org" + first_link.get('href')
    return

def main():
    url = 'https://en.wikipedia.org/wiki/Special:Random'

    article_selector(url)

    return

if __name__ == "__main__": main()