from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, SoupStrainer
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_random_wikipedia_article():
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/John_Locke")
    return driver

def finder(driver):
    while True:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        title_tag = soup.find('title')
        print(title_tag.text.strip())

        if title_tag.text.strip() == "Philosophy - Wikipedia":
            print("Reached Philosophy page!")
            break

        link = soup.findAll('a', class_="mw-redirect")

        print(link)

        if link:
            link_xpath = "//a[@class='mw-redirect' and @href='" + link[1].get('href') + "']"
            # Wait for the link to be clickable
            link_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, link_xpath))
            )

            link_element.click()

            # Wait for the page to be updated
            WebDriverWait(driver, 10).until(EC.staleness_of(link_element))

        else:
            print("No link found with the specified criteria.")

def main():
    driver = open_random_wikipedia_article()
    finder(driver)

if __name__ == "__main__":
    main()
