import json
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
import time

from config import REFRESH_INTERVAL
from models import Specifications, Product, Site


class PriceTracker:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def load_products_from_json(self, json_filename):
        with open(json_filename, 'r') as json_file:
            products_data = json.load(json_file)

        for product_data in products_data:
            product = Product(
                name=product_data['name'],
                specifications=Specifications(**product_data['specifications']),
                sites=[Site(**site_data) for site_data in product_data['sites']]
            )
            self.add_product(product)
    def track_prices(self):
        while True:
            for product in self.products:
                print(f"Tracking prices for {product.name}")
                for site in product.sites:
                    try:
                        price = site.scraper.fetch_price(site.url)
                        print(f"{site.name} - {product.name} Price: {price}")
                    except Exception as e:
                        print(f"Error fetching price from {site.name}: {str(e)}")

                print("-" * 40)

            time.sleep(int(REFRESH_INTERVAL))  # Adjust the interval (in seconds) between price checks



