import sys
import os
from selenium import webdriver

# Dict of the sites to search. Adjust as desired.
#	key = website URL; value = HTML name of input box element
sites_to_search = {
	"https://unsplash.com/": "searchKeyword",
	"https://www.pixabay.com": "q",
	"https://stocksnap.io": "main-search",
	"https://burst.shopify.com": "q",
	"https://www.gratisography.com": "s"
}

if __name__ == "__main__":
	# Store the desired phrase to search
	search_term = " ".join(sys.argv[1:])
	if search_term == "": 
		print("No search phrase entered.")
	else:
		try:
			browser = webdriver.Chrome()
		except Exception as err:
			print(f"Can't open Chrome browser: '{err}'")
		else:
			print(f"***** Sites being searched for '{search_term}': ***** ")
			flag_opened = False
			for site in sites_to_search:
				print(f"- {site}")
				try:
					if not flag_opened:
						# Open the 1st URL in a new browser window
						browser.get(site)
						flag_opened = True
					else: 
						# Open a new tab for next URL
						browser.execute_script(f"window.open('{site}');")
						browser.switch_to.window(browser.window_handles[-1])
					# Access input box element on website, by name
					python_button = browser.find_elements_by_xpath(f"//input[@name='{sites_to_search[site]}']")[0]
					#	Note: You can also access the input box element by the full xpath. 
					# 		To get full xpath of an HTML element on a website, first "Inspect" the element, 
					# 		then right click on "Copy" -> "Copy XPath".

					python_button.send_keys(search_term)
					python_button.send_keys(u'\ue007')	# keycode for ENTER in selenium
					print("\tSuccess!\n")
				except Exception as err:
					print(f"\tCan't search {site} properly.\n\tError: '{err}'", "\n")
			print("***** Done searching. *****", "\n")