# open_image_websites

## Motivation
As a blog writer, whenever I finish writing and editing a post, the last step is always to search for some royalty-free images / pictures, to make the post more readable.

And this ALWAYS involves going to my browser, typing in the same URLs across multiple tabs, and searching for a particular term / phrase.

This definitely leaves room to automate.



## Install/Setup 

```bash
git clone "https://github.com/________________.git"
cd open_image_websites
pip install -r requirements.txt
source commands.sh
```

Note #1: You also need to install the "Latest stable release" version of chromedriver, at: https://chromedriver.chromium.org/, and add it to $PATH.

Note #2: "source commands.sh" only sets the "search" function as a terminal command for the current terminal session; need to rerun on every new terminal session. To have the command persist, add the *open_image_websites* directory to $PATH as well.



## Usage

To run the script, type in "search *search_term_or_phrase*"



## 1st stage, Completed on Dec 4th, 2019:
Script will open up these websites:

	- https://www.upsplash.com
	- https://www.pixabay.com
	- https://stocksnap.io
	- https://burst.shopify.com
	- https://www.gratisography.com
and autosearch each site for the desired phrase. 

The program will then terminate.

(Note: Super easy to tweak the dictionary variable to include more or less image sites to search.)


### Potential Developments
1. Currently having difficulty searching:
	- https://www.pexels.com
	- https://www.reshot.com
	
	Trying to retrieve their input boxes gives a "Element not interactable" message.
	Tried *find_element_by_css_selector* instead of *find_elements_by_xpath*.
2. Don't terminate the program until the user *quits*. In the meantime, allow the user to re-search all the sites for a new term / phrase. 

(i.e. user didn't find a picture that fit his/her needs on the initial search)
