import sys
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

# Note: add try-except to make the code more bulletproof

print("*** Inside search_images.py: ***")

# sites_to_search = {
# 	"https://unsplash.com/": "searchKeyword"
# }


search_term = ""
for i in range(1, len(sys.argv)):
	search_term += sys.argv[i] + " "

search_term = search_term.strip()

print(search_term)

if search_term != "":
	browser = webdriver.Chrome()
	browser.get("https://unsplash.com/")
	# Clicking on the element by xpath
#	python_button = browser.find_elements_by_xpath("//*[@id='SEARCH_FORM_INPUT_homepage-header-big']")[0]
	# Note: To get the xpath of an HTML element on a website, 
	#	first "Inspect" the element, then right click on "Copy" -> "Copy XPath"
	# Note: Can also click on an element by the element's name
	python_button = browser.find_elements_by_xpath("//input[@name='searchKeyword']")[0]
	python_button.send_keys(search_term)
	python_button.send_keys(u'\ue007')	# u'\ue007' is the keycode for ENTER in selenium

	# Open a new tab to specified link
	browser.execute_script("window.open('https://www.pixabay.com');")
	browser.switch_to.window(browser.window_handles[-1])
#	python_button = browser.find_elements_by_xpath("//*[@id='hero']/div[3]/form/div/span/input")[0]
	python_button = browser.find_elements_by_xpath("//input[@name='q']")[0]
	python_button.send_keys(search_term)
	python_button.send_keys(u'\ue007')

	browser.execute_script("window.open('https://stocksnap.io');")
	browser.switch_to.window(browser.window_handles[-1])
#	python_button = browser.find_elements_by_xpath("//*[@id='main-search-form']/input")[0]
	python_button = browser.find_elements_by_xpath("//input[@name='main-search']")[0]
	python_button.send_keys(search_term)
	python_button.send_keys(u'\ue007')

	browser.execute_script("window.open('https://burst.shopify.com');")
	browser.switch_to.window(browser.window_handles[-1])
#	python_button = browser.find_elements_by_xpath("//*[@id='search_search']")[0]
	python_button = browser.find_elements_by_xpath("//input[@name='q']")[0]
	python_button.send_keys(search_term)
	python_button.send_keys(u'\ue007')

	browser.execute_script("window.open('https://www.gratisography.com');")
	browser.switch_to.window(browser.window_handles[-1])
#	python_button = browser.find_elements_by_xpath("//*[@id='s']")[0]
	python_button = browser.find_elements_by_xpath("//input[@name='s']")[0]
	python_button.send_keys(search_term)
	python_button.send_keys(u'\ue007')

else: 
	print("No search phrase entered.")

# def create():
#     python_button = browser.find_elements_by_xpath("//input[@name='login'")[0]
#     python_button.click()

# browser.close()

# if __name__ == "__main__":
#     create()








