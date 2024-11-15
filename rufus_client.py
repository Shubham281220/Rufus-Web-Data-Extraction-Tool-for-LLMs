from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import time
import os

class RufusClient:
    def __init__(self, api_key=None):
        # Optional: Handle the API key (currently not used for functionality)
        self.api_key = api_key or os.getenv("Rufus_API_KEY")
        
        # Initialize Playwright
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)

    # Function to scrape the page, with depth and prompt
    def scrape(self, url, depth=2, prompt="HR in San Francisco"):
        crawled_data = []
        visited_urls = set()

        # Recursive scraping function
        def scrape_page(url, current_depth):
            if current_depth > depth or url in visited_urls:
                return
            visited_urls.add(url)

            page = self.browser.new_page()
            page.goto(url)
            time.sleep(2)
            soup = BeautifulSoup(page.content(), 'html.parser')
            
            # Extract relevant content based on the prompt
            relevant_content = self._extract_relevant_content(soup, prompt)
            
            if relevant_content:
                crawled_data.append({
                    'url': url,
                    'title': soup.title.string if soup.title else 'No title',
                    'content': relevant_content
                })
            page.close()

            # Follow links within the depth limit
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith("http") and not any(href.endswith(ext) for ext in ['.pdf', '.jpg', '.jpeg', '.png', '.zip']):
                    scrape_page(href, current_depth + 1)

        scrape_page(url, 0)
        return crawled_data

    # Function to filter content based on the prompt keywords
    def _extract_relevant_content(self, soup, prompt):
        sections = []
        keywords = prompt.lower().split()  # Simple splitting based on the prompt
        for section in soup.find_all(['h2', 'h3', 'p']):
            text = section.get_text().strip()
            if any(keyword in text.lower() for keyword in keywords):
                sections.append({
                    'section_title': section.name,
                    'text': text
                })
        return sections if sections else None

    # Save data to JSON with structured formatting
    def save_to_json(self, data, filename='output.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to '{filename}'")

    def close(self):
        self.browser.close()
        self.playwright.stop()

