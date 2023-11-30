
import requests
from bs4 import BeautifulSoup

def article_selector(url): 

    n = -1
    title_list = []

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
            #these links can't be included because they appear as the first link in tons of articles, may need to add to this
            excluded_hrefs = ["/wiki/Arabic_language", "/wiki/Ancient_Greek_language", "/wiki/Ancient_Greek", "/wiki/Greek_language", "/wiki/Latin", "/wiki/Latin_language", "/wiki/Russian_language", 
                              "/wiki/Devanagari", "/wiki/Hindi_language", "wiki/Hindi", "/wiki/Spanish_language", "/wiki/French_language", "wiki/M%C4%81ori_language",
                              "/wiki/German_language", "/wiki/American_English", "/wiki/British_English", "/wiki/English_language", "/wiki/Persian_language", "/wiki/Hungaran_language",
                              "/wiki/Korean_language", "/wiki/Simplified_Chinese_characters", "/wiki/Traditional_Chinese_characters", "/wiki/Chinese_characters", "/wiki/Pinyin", "/wiki/Chinese_language",
                              "/wiki/Japanese_language", "/wiki/Italian_language", "/wiki/Portugese_language", "/wiki/Romanian_language", "/wiki/Danish_language", "/wiki/Swedish_language",
                              "/wiki/Norwegian_language", "/wiki/Ukranian_language", "/wiki/Czech_language", "/wiki/Old_French", "/wiki/Northern_Sami_language"]
            for l in links:
                href = l.get('href','')
                if (href.startswith('/wiki/') and
                        not (href.startswith('/wiki/Help:') or 
                            href.startswith('/wiki/File:') or
                            href.startswith('wiki/ISO') or
                            href in excluded_hrefs
                        )): selected_links.append(l)

            return selected_links


        #gets list of filtered links from 1st paragraph, chooses the 1st one as our "first link" if 1st paragraph has no links, chooses the next paragraph
        def select_first_link():
            valid_links = []
            i = 0
            while len(valid_links) == 0:
                valid_links = filter_links(selected_paragraphs[i].findAll('a'))
                i += 1

            if len(valid_links) > 0:
                first_link = valid_links[0]
                return first_link
            else: return None
        
        first_link = select_first_link()

        #make title readable
        title_text = soup.find('title').text[:-12]
        
        #loop identifier, adds all links to a list and if there are repeats, breaks and claims it's a loop
        if title_text in title_list:
            print(title_text)
            print("A loop has occured!\n")
            break
        title_list.append(title_text)


        #check if we are at the Philosophy page, if so stop, and say how long it took to get there.
        if title_text == 'Philosophy':

            print(title_text)
            print("You made it to Philosophy!")
            print ("That took " + str(n) + " steps.\n")

            break


        #print the page title and update the url with our first_link
        print(title_text)
        url = "https://en.wikipedia.org" + first_link.get('href')
    return

def main():
    url = 'https://en.wikipedia.org/wiki/Special:Random'

    article_selector(url)

    return

#if __name__ == "__main__": main()

for i in range(30): main()