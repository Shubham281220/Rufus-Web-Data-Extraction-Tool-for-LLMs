# Rufus – Web Data Extraction Tool for LLMs

## Project Overview
Rufus is an intelligent web data extraction tool designed for use in Retrieval-Augmented Generation (RAG) systems. It dynamically scrapes web content and synthesizes it into structured documents, making it easier to integrate with downstream LLM applications. This tool is designed to crawl websites, extract relevant content based on user-defined prompts, and output the data in a structured format (JSON).

## Features
- **Website Crawling**: Crawls websites up to a specified depth.
- **Selective Scraping**: Extracts relevant data based on a user-defined prompt (e.g., "Find information about HR in San Francisco").
- **Document Synthesis**: Outputs structured documents in JSON format.
- **Error Handling**: Gracefully handles errors such as timeouts or inaccessible pages.

---

## Project Setup

### 1. **Set Up Virtual Environment**

To ensure your project runs smoothly and avoids dependency conflicts, it's best to create and activate a virtual environment.

1. **Create a Virtual Environment**:
   Open your terminal and run the following command:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### 2. **Install Required Dependencies**

Once the virtual environment is activated, you'll need to install the necessary dependencies.

1. **Install Playwright and Other Libraries**:

   The project relies on **Playwright** (for web scraping) and **BeautifulSoup** (for content parsing).

   Run the following command to install the required libraries:

   ```bash
   pip install playwright beautifulsoup4
   ```

2. **Install Playwright Browsers**:

   Playwright requires browser binaries to function. You can install them by running:

   ```bash
   playwright install
   ```

### 3. **Repository Structure**

Your GitHub repository should have the following structure:

```
Rufus-Project/
│
├── rufus.py                # The main web scraper file
├── rufus_client.py         # API version of the scraper
├── run_rufus.py            # Script to run the scraper
├── structured_output.json  # Output from rufus.py
├── structured_output-2.json # Output from rufus_client.py and run_rufus.py
├── README.md               # Project Documentation
└── requirements.txt        # List of Python dependencies
```

---

## How to Run the Code

### 1. **Clone the Repository**

If you haven't already cloned the repository, run the following command:

```bash
git clone <repository_url>
cd Rufus-Project
```

### 2. **Activate the Virtual Environment**

Before running the code, make sure the virtual environment is activated:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. **Run `rufus.py` (Traditional Script)**

`rufus.py` is the original scraper that runs on its own.

To run `rufus.py`, simply use:

```bash
python rufus.py
```

It will scrape data from the predefined URL (`https://www.sfgov.org`) and save the result in `structured_output.json`.

### 4. **Run `rufus_client.py` (API Version)**

`rufus_client.py` is designed as an API that can be used to integrate with other systems, like RAG pipelines.

To run `rufus_client.py`, use the following script (`run_rufus.py`):

1. **Run the `run_rufus.py` Script**:

   ```bash
   python run_rufus.py
   ```

2. **How it Works**:
   - The script instantiates the `RufusClient` class, specifies the `url`, `depth`, and `prompt`, and starts the scraping process.
   - The extracted data will be saved in `structured_output-2.json`.

### 5. **View the Output**

The output from both scripts will be saved in JSON format:

- `structured_output.json`: Output from `rufus.py`.
- `structured_output-2.json`: Output from `rufus_client.py` (API version).

---

## Improvements and Suggestions

While the current implementation works well, here are some potential improvements you might want to consider:

1. **Add Logging**: 
   - Although not necessary for the current version, adding logs would help you debug the scraping process, especially if you're dealing with large websites or complex scraping scenarios.
   - Use Python’s built-in `logging` library to log important actions like page visits, timeouts, and retries.

2. **Implement Concurrency/Parallelism**:
   - To make the scraper faster, you could implement parallel scraping using threads or multiprocessing. Playwright supports async operations, and you could switch to `asyncio` for more efficient crawling.
   - Consider using tools like `asyncio` or `concurrent.futures` to handle multiple requests simultaneously.

3. **Improve Selective Scraping**:
   - Instead of filtering by just a simple keyword match, you can use more advanced methods (e.g., regular expressions or AI-based models) to better extract content based on the user's prompt.

4. **Error Handling Enhancements**:
   - Add more error handling for edge cases such as inaccessible pages, malformed URLs, or incomplete HTML content.
   - Consider implementing retries with exponential backoff for better robustness.

5. **Rate Limiting**:
   - To prevent hitting websites too aggressively, implement rate limiting to avoid being blocked.
   - You can add delays or random intervals between requests.

6. **Headless Browser Configuration**:
   - If you'd like to see the scraping process visually, you can disable the headless mode (i.e., open the browser window during scraping).
   - Modify the `launch()` method to run in non-headless mode:
     ```python
     self.browser = self.playwright.chromium.launch(headless=False)
     ```

---

## Final Remarks

- **Code Quality**: The code is designed to be modular and flexible. The `scrape` function can easily be adapted to different websites or additional content extraction needs.
- **Scalability**: The project structure is scalable, and you can add more functions (e.g., handling additional HTML tags or dynamic content loading).
- **Submission**: This README, along with the project files, should be sufficient for submission. Make sure you upload the final working code to GitHub along with this documentation.

---

This README is now ready for your project repository on GitHub. If you need to include additional steps or clarifications, you can always modify this document further.

Let me know if you need any changes or additions!
```

