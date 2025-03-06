# Naruto Jutsu Scraper

## Overview
This project is a web scraper built using **Scrapy** and **BeautifulSoup** to extract data about jutsu (techniques) from the **Naruto Fandom Wiki**.

## Features
- Scrapes jutsu names, classifications, and descriptions.
- Navigates multiple pages to fetch all jutsu entries.
- Uses **Scrapy** for efficient crawling.
- Parses HTML with **BeautifulSoup** to extract structured data.

## Installation
### Prerequisites
Make sure you have **Python 3.x** installed.

### Install Dependencies
```bash
pip install scrapy beautifulsoup4
```

## Usage
1. Clone this repository:
```bash
git clone https://github.com/Fliptoss/web_scraping
cd YOUR-REPO
```
2. Run the scraper:
```bash
scrapy runspider scraper.py -o jutsu.json
```
3. The scraped data will be saved in `jutsu.json`.

## How It Works
- The scraper starts at the **Naruto Fandom Wiki Jutsu page**.
- Extracts links to individual jutsu pages.
- Fetches **name, classification, and description** for each jutsu.
- Saves the data in JSON format.

## Example Output
```json
{
    "jutsu_name": "Rasengan",
    "jutsu_type": "Ninjutsu",
    "jutsu_description": "A powerful spiraling sphere of chakra."
}
```

## License
This project is for educational purposes only. Data is scraped from Naruto Fandom Wiki, which holds copyright to the content.

## Contributions
Feel free to fork the repository and submit pull requests!

