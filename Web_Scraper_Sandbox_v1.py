import requests
from bs4 import BeautifulSoup
import json
import csv


def fetch_quotes_from_page(url):
    """Scrapes all quotes from a single page."""
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return [], None

    soup = BeautifulSoup(response.text, 'html.parser')
    quote_containers = soup.find_all('div', class_='quote')

    quotes = []
    for container in quote_containers:
        quote_text = container.find('span', class_='text').get_text(strip=True)
        author = container.find('small', class_='author').get_text(strip=True)
        quotes.append({
            "quote": quote_text,
            "author": author
        })

    next_button = soup.find('li', class_='next')
    next_url = "https://quotes.toscrape.com" + next_button.a['href'] if next_button else None

    return quotes, next_url


def scrape_all_quotes(start_url="https://quotes.toscrape.com/"):
    """Loops through all pages and scrapes all quotes."""
    all_quotes = []
    url = start_url
    while url:
        quotes, url = fetch_quotes_from_page(url)
        all_quotes.extend(quotes)
    return all_quotes


def save_to_txt(quotes, filename="scraped_quotes.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for q in quotes:
            f.write(f"{q['quote']} - {q['author']}\n\n")
    print(f"✅ Saved {len(quotes)} quotes to {filename}")


def save_to_json(quotes, filename="scraped_quotes.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)
    print(f"✅ Saved {len(quotes)} quotes to {filename}")


def save_to_csv(quotes, filename="scraped_quotes.csv"):
    with open(filename, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author"])
        writer.writeheader()
        writer.writerows(quotes)
    print(f"✅ Saved {len(quotes)} quotes to {filename}")


def main():
    print("🔍 Scraping quotes...")
    quotes = scrape_all_quotes()

    # Change this to 'json' or 'csv' as needed
    output_format = 'txt'

    if output_format == 'json':
        save_to_json(quotes)
    elif output_format == 'csv':
        save_to_csv(quotes)
    else:
        save_to_txt(quotes)


if __name__ == "__main__":
    main()

