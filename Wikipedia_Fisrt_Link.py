import requests
from bs4 import BeautifulSoup

def article_selector(url): 

    n = 0

    while n < 10:
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


        print(selected_paragraphs[0].text)
        print(selected_paragraphs[0].get('class'))

        #update the url with the first link href

        if title_text == 'Philosophy - Wikipedia':

            print("You made it to Philosophy!")
            print ("That took " + str(n) + " steps.")

            break


        #url = "https://en.wikipedia.org" + first_link.get('href')
    return

def main():
    url = 'https://en.wikipedia.org/wiki/Special:Random'

    article_selector(url)

    return

if __name__ == "__main__": main()