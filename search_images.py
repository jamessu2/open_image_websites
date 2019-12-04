import sys
import os
from selenium import webdriver

# Note: add try-except to make the code more bulletproof

print("*** Inside search_images.py: ***")

search_term = ""
for i in range(1, len(sys.argv)):
	search_term += sys.argv[i] + " "

print(search_term)

browser = webdriver.Chrome()
browser.get("http://www.github.com/login")


# def create():
#     python_button = broswer.find_elements_by_xpath("//input[@name='login'")[0]
#     python_button.click()

# browser.close()

# if __name__ == "__main__":
#     create()








