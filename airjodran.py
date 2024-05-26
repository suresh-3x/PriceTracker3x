import requests
from datetime import datetime, time
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML

# Define URL and desired check times
url = "https://www.nike.com/in/launch/t/air-jordan-1-mid-se-white-black"
night_checks = [time(18, 0), time(0, 0), time(3, 0)]
day_checks = [time(i, 0) for i in range(6, 19)]  # Checks every hour from 6 AM to 6 PM

def check_stock():
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Check for "sold out" text based on potential presence in buttons or specific elements
  sold_out_elements = soup.find_all('button', text="Sold Out")  # Look for buttons with "Sold Out" text
  # You can add additional checks for other elements or text variations
  is_out_of_stock = len(sold_out_elements) > 0

  print(f"{datetime.now()}: Stock status - {'In Stock' if not is_out_of_stock else 'Out of Stock'}")

while True:
  now = datetime.now().time()
  if True or now in night_checks or now in day_checks:
    check_stock()
  # Schedule next check after 1 hour and 30 minutes (adjust as needed)
  #time.sleep(60 * 60 * 1.5)

