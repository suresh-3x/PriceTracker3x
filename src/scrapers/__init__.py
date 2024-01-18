import requests
from bs4 import BeautifulSoup
import json
import re

class SiteScraper:
    def fetch_price(self, url):
        raise NotImplementedError("Subclasses must implement fetch_price method")


class AmazonScraper(SiteScraper):
    def fetch_price(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Replace this with the actual logic to extract Amazon price
        # Example: Extract Amazon price from the real website
        price_element = soup.find('span', {'id': 'priceblock_ourprice'})
        price = price_element.text.strip() if price_element else "Price not available"

        return price


class FlipkartScraper(SiteScraper):
    def fetch_price(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Replace this with the actual logic to extract Flipkart price
        # Example: Extract Flipkart price from the real website
        price_element = soup.find('div', {'class': '_30jeq3'})
        price = price_element.text.strip() if price_element else "Price not available"

        return price

class CromaScraper(SiteScraper):
    def fetch_price(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract Croma price from the real website
        # Find the script tag containing the JSON data
        script_tag = soup.find('script', type='application/ld+json')
        script_content = script_tag.contents[0].strip()

        # Extract valid JSON strings using regex
        json_strings = re.findall(r'{[^{}]*}', script_content)


        json_data = json.loads(json_strings[1])
        # Extract the price from the JSON data
        price = json_data['price']
        currency = json_data['priceCurrency']

        return f"{currency}: {price}"