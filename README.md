# open_image_websites

As a [blog](https://askmeabetterquestion.com/) writer, whenever I finish writing a post, the last step is always to search for some images / pictures – i.e. make the post look better.

And this ALWAYS involves going to my browser, typing in the same-old URLs to royalty-free image websites (across multiple tabs), and searching for a particular term / phrase on each site.

A perfect task to automate.



## Install/Setup 

```bash
git clone "https://github.com/jamessu2/open_image_websites.git"
cd open_image_websites
pip install -r requirements.txt
source commands.sh
```

**Note #1**: You also need to install the *"Latest stable release"* version of [chromedriver](https://chromedriver.chromium.org/), and add it to `$PATH`.

**Note #2**: `source commands.sh` only sets the `search` function as a terminal command for the current terminal session. You'd need to rerun on every new terminal session. 

To have the command persist, add the *open_image_websites* directory to `$PATH` as well.



## Usage

To run the script, type in `search <term>`



## Functionality
Script will open up these websites:

- https://www.upsplash.com
- https://www.pixabay.com
- https://stocksnap.io
- https://burst.shopify.com
- https://www.gratisography.com

and autosearch each site for the desired term/phrase, then terminate. 

(Super easy to add / remove image sites to search.)


## Future Developments
*1st stage: completed Dec 4th, 2019.*

Next-level functionality:

1. Figure out how to autosearch these sites:
	- https://www.pexels.com
	- https://www.reshot.com
	
	Trying to retrieve their input boxes gives an *"Element not interactable"* error message.
	Tried Python's `find_element_by_css_selector` instead of `find_elements_by_xpath`, to no avail.

2. Next-level functionality: Allow the user to re-search all the sites for a new term / phrase. Don't terminate until the user **quits**.

	(i.e. need to run more searches)
