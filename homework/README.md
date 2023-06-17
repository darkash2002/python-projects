# Overview
This project implements a system that scrape given a URL.
The system receives a URL and some arguments for the wanted scraping (usage explanation and example later), and saves 
the information obtained from the given URL.

# Parameter Explanation
url: the URL that you want to start your scraping.
max_url: the maximum URLs you want to obtain from a single website
depth: the depth you want to get in. Meaning - how many layers of URL you want to scrape. 
        Now we support only in 0 (no depth), 1 (getting inside every URL from the initial search), 2 (5 layers deep)
unique (filter_duplicate_urls): filtering duplicate URLs. Can help you save space and performance.
filter_duplicate_urls_same_html: if you want to filter the URLs inside HTML
##### example:
>> python3.9 main.py --url http://example.com --max_url 5 --depth 0 --unique



# Flow
1. the user runs main.py as the example indicates
2. the user input parsed and checked
3. a Scraper is created with the user parameters
4. the Scraper checks the depth the user want
5. if the depth check went well, the Scraper will create URL object
6. the Scraper will save the file using a method from the URL object
7. the function will consider if the file already saved and the user don't want any duplicate files
8. if the URL is unique or the user want to save every URL (dups included) - it will trigger a method that gets the HTML
content
9. the Scraper extract (by regex) the URLs from the HTML
10. the Scraper iterate over every URL with the same process (from stage 4) until the depth is bigger then the depth 
the user inputs 


# Architecture
- main.py
- scraper.py
- url.py
- utils.py

#### main.py:
Handling user input and runs a Scraper accordingly.

#### scraper.py:
Implements class that represent Scraper. 
The attributes are depth and filter_duplicate_urls because those parameters relevant to the Scraping proccess.
The method is simple: recursive scraping. 

#### url.py:
Implements class that represent URL.
The attribute is the URL address itself.
The methods are working on URL address - get the HTML content from the URL address, saves the URL to an orgenized 
file system, and extract the URLs from the HTML content.

### TODO's:
1. Performance: using concurrent.futures correctly
2. testing
3. Features: using BeautifulSoup library for more features
4. logging (instead of printing)
5. using DB for the file saving format ("unlock" the ability to filter duplicate data and store more meta-data in general)
6. using better API
7. Zip the files to save space

For performance:
I tried using futures to iterate over some URLs at the same time, it costs more time and CPU than the current code.
ChatGPT recommended using cProfile to debug this.