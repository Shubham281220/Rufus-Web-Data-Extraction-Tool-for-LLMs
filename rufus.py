from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

# Initialize Playwright
def init_playwright():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    return browser

# Crawl pages up to a specified depth, filtering by prompt keywords
def crawl_page(browser, url, depth=2, prompt="HR in San Francisco"):
    crawled_data = []
    visited_urls = set()

    def scrape(url, current_depth):
        if current_depth > depth or url in visited_urls:
            return
        visited_urls.add(url)

        page = browser.new_page()
        page.goto(url)
        time.sleep(2)
        soup = BeautifulSoup(page.content(), 'html.parser')
        
        # Selective Scraping based on prompt
        relevant_content = extract_relevant_content(soup, prompt)
        
        if relevant_content:
            crawled_data.append({
                'url': url,
                'title': soup.title.string if soup.title else 'No title',
                'content': relevant_content
            })
        page.close()

        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            if href.startswith("http") and not any(href.endswith(ext) for ext in ['.pdf', '.jpg', '.jpeg', '.png', '.zip']):
                scrape(href, current_depth + 1)

    scrape(url, 0)
    return crawled_data

# Function to filter content based on the prompt keywords
def extract_relevant_content(soup, prompt):
    sections = []
    keywords = prompt.lower().split()
    for section in soup.find_all(['h2', 'h3', 'p']):
        text = section.get_text().strip()
        if any(keyword in text.lower() for keyword in keywords):
            sections.append({
                'section_title': section.name,
                'text': text
            })
    return sections if sections else None

# Save data to JSON with structured formatting
def save_data_to_json(data, filename='structured_output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Main function
def main():
    url = "https://www.sfgov.org"
    depth = 2
    prompt = "HR in San Francisco"

    browser = init_playwright()
    
    try:
        data = crawl_page(browser, url, depth, prompt)
        save_data_to_json(data, 'structured_output.json')
        print("Data saved to 'structured_output.json'")
    finally:
        browser.close()

if __name__ == "__main__":
    main()
