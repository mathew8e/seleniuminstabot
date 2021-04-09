from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

#check if a headless switch is
chrome_options = Options()
if 1 in range(-len(sys.argv), len(sys.argv)):
    if sys.argv[1] == "--headless":
        chrome_options.headless = True

dr = webdriver.Chrome(options=chrome_options)
