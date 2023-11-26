
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options = Options()
options.binary = FirefoxBinary(r'/usr/bin/firefox')
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/Data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")
driver = webdriver.Firefox(executable_path=r'/snap/bin/geckodriver', options=options)

driver.get("https://en.wikipedia.org/wiki/Special:Random")