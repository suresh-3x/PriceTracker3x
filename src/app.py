from models import Product, Site, Specifications
from price_tracker import PriceTracker

if __name__ == "__main__":
    price_tracker = PriceTracker()
    # Add products to the PriceTracker
    price_tracker.load_products_from_json("src/products.json")
    # Start tracking prices
    try:
    	price_tracker.track_prices()
    except KeyboardInterrupt as ex:
        print("___STOPPED___")
    except Exception as e:
        print(e)
