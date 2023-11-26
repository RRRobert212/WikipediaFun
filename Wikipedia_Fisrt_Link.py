#A program that opens a random wikipedia article and then clicks the first link until it arrives at the philosophy article
#It should print the first article, the number of steps it took to get to philosophy, and perhaps the names of the articles inbetween
#Can eventually add some sort of graph or something to display relationships between articles

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import random

def open_random_wikipedia_article():
    # Specify the path to the Firefox binary
    firefox_binary_path = '/usr/bin/firefox'

    # Create Firefox options
    firefox_options = Options()
    firefox_options.binary_location = firefox_binary_path

    # Create a Firefox WebDriver with the specified options
    driver = webdriver.Firefox(options=firefox_options)

    # Open a random article on Wikipedia
    driver.get("https://en.wikipedia.org/wiki/Special:Random")

    return driver

def find_next_link(driver):
    # Wait for the page to load
    time.sleep(2)

    # Get the page source
    page_source = driver.page_source

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all non-italicized and non-paranthesized links
    candidate_links = soup.find_all('a', {'class': False, 'href': True})
    valid_links = [link for link in candidate_links if not is_italicized(link) and not is_paranthesized(link)]

    if not valid_links:
        # If no valid links are found, close the browser and return None
        driver.quit()
        return None

    # Choose a random valid link
    random_link = random.choice(valid_links)

    # Click the link
    random_link.click()

    return driver

def is_italicized(link):
    return link.find('i') is not None or link.find('em') is not None

def is_paranthesized(link):
    return link.find('span', {'class': 'mw-editsection-bracket'}) is not None

if __name__ == "__main__":
    # Open a random article
    driver = open_random_wikipedia_article()

    # Specify the title of the article you want to reach
    target_article = "Your Target Article Title"

    # Loop until the target article is reached
    while True:
        # Find the next link on the current page
        driver = find_next_link(driver)

        if driver is None:
            print("No valid links found. Exiting.")
            break

        # Check if the current article is the target article
        if target_article.lower() in driver.title.lower():
            print(f"Target article '{target_article}' reached. Exiting.")
            break

    # Close the browser
    driver.quit()
