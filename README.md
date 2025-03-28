# 📝 Quote Scraper – Command Line Web Scraper in Python

A Python script that scrapes quotes from [https://quotes.toscrape.com](https://quotes.toscrape.com) using BeautifulSoup and saves them to a file — now with CLI support!

---

### 🔍 What It Does

- Scrapes **all pages** from the website
- Extracts quotes and their authors
- Lets you choose output format: `.txt`, `.json`, or `.csv`
- Lets you name your output file via the command line

---

### ▶️ How to Run

1. **Clone the repo**:

   ```bash
   git clone https://github.com/W-Riley-01/quote-scraper.git
   cd quote-scraper

2. Install dependencies:
pip install -r requirements.txt

3. Run the Scaper
python quote_scraper.py

⚙️ Command-Line Options
You can customize the output format and filename:
python quote_scraper.py --format json             # Save as JSON
python quote_scraper.py --format csv              # Save as CSV
python quote_scraper.py --format txt --output my_quotes.txt

📁 Output Examples
scraped_quotes.txt:

“The world as we have created it is a process of our thinking.” – Albert Einstein

scraped_quotes.json:
[
  {
    "quote": "The world as we have created it is a process of our thinking.",
    "author": "Albert Einstein"
  }
]

quote,author
"The world as we have created it...",Albert Einstein


🧠 Why I Built This
I created this project to learn and demonstrate:

Web scraping with requests and BeautifulSoup

Pagination scraping (multi-page data)

Output formatting in multiple file types

Using argparse for clean command-line interfaces

It’s a small but flexible tool — and a foundation for more powerful scraping projects.

🛠 Built With
Python 3.x

requests

beautifulsoup4

argparse

json and csv (standard libraries)

🔐 Ethics Note
This scraper targets a demo site made specifically for scraping practice:
https://quotes.toscrape.com — no scraping of real or sensitive websites.
