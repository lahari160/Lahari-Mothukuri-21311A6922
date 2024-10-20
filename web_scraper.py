import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.text  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def extract_webpage_data(url):
    content = fetch_webpage(url)
    if content is None:
        return
    
    soup = BeautifulSoup(content, 'html.parser')
    
    title = soup.title.string if soup.title else "No title found"
    print(f"Title: {title}\n")
    
    print("Headings:")
    for level in ['h1', 'h2', 'h3']:
        headings = soup.find_all(level)
        for heading in headings:
            print(f"{level}: {heading.get_text()}")
    print()
    
    print("Links:")
    links = soup.find_all('a', href=True)
    for link in links:
        text = link.get_text(strip=True)  
        href = link['href']  
        print(f"Text: '{text}' - URL: {href}")
    print()
    
    print("Images:")
    images = soup.find_all('img', src=True)
    for img in images:
        print(f"Image URL: {img['src']}")
    print()

if __name__ == "__main__":
    url = input("Enter the URL of the webpage you want to scrape: ")
    extract_webpage_data(url)
