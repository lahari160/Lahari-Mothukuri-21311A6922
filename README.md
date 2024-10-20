# Python Web Scraper

## About the code
This Python script is a web scraper that fetches and extracts specific information from a webpage, including:
1. The title of the page.
2. Headings (h1, h2, h3).
3. Hyperlinks (anchor tags).
4. Image URLs (img tags).

# Requirements
- Python 
- Libraries:
  - requests (pip install requests)
  - bs4 (BeautifulSoup) (pip install beautifulsoup4)

## Installation
You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4

##Code Run
1. Save the code with name web_scraper.py
2. Run the code
3. Enter url(uniform resource locator) of the web page

IMP NOTE:

The current implementation of the web scraper works well for static web pages, where the HTML content is already fully loaded when the page is accessed. However, dynamic web pages (such as those that load content via JavaScript after the initial HTML has been served) will not be fully scraped using this method because the additional content is not loaded by just making an HTTP request.
