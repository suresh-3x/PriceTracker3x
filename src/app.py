from price_tracker import PriceTracker
from models import Product, Specifications, Site

if __name__ == "__main__":
    price_tracker = PriceTracker()



    # Add products to the PriceTracker
    price_tracker.load_products_from_json('./products.json')

    # Start tracking prices
    price_tracker.track_prices()
