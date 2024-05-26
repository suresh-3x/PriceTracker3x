import time
from dataclasses import dataclass, field

import requests
from bs4 import BeautifulSoup

from scrapers import AmazonScraper, CromaScraper, FlipkartScraper


@dataclass
class Specifications:
    color: str
    size: str
    # Add more specifications as needed


@dataclass
class Site:
    name: str
    url: str
    scraper: "SiteScraper" = field(init=False, default=None)

    def __post_init__(self):
        if self.name.lower() == "amazon":
            self.scraper = AmazonScraper()
        elif self.name.lower() == "flipkart":
            self.scraper = FlipkartScraper()
        elif self.name.lower() == "croma":
            self.scraper = CromaScraper()
        else:
            raise ValueError(f"Unsupported site: {self.name}")


@dataclass
class Product:
    name: str
    specifications: Specifications
    sites: list[Site]
