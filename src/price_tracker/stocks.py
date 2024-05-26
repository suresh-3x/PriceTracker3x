import requests
from bs4 import BeautifulSoup

def get_top_movers(url, gainers=True):
  """
  Fetches top gainers (or losers) data from the NSE website.

  Args:
      url (str): URL of the NSE top movers page for gainers or losers.
      gainers (bool, optional): Whether to fetch data for gainers (True) or losers (False). Defaults to True.

  Returns:
      list: List of dictionaries containing information about top movers.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'lxml')

  # Identify table based on gainers/losers
  if gainers:
    table = soup.find('table', class_='view tgainer')
  else:
    table = soup.find('table', class_='view tloser')

  if not table:
    print(f"Error: Couldn't find table for {('gainers' if gainers else 'losers')}")
    return []

  # Extract data from table rows
  rows = table.find_all('tr')[1:]  # Skip header row
  top_movers = []
  for row in rows[:20]:  # Get top 20
    data = row.find_all('td')
    top_movers.append({
      'symbol': data[0].text.strip(),
      'change': data[1].text.strip(),
      'percentage': data[2].text.strip(),
    })
  return top_movers

# Example usage
nse_gainers_url = "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm?symbol=INDEX%20NIFTY&segmentLink=17&symbolCount=2&series=EQ&dataType=PRICEVOLUMEDELIVERY&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERY&dataType=PRICEVOLUMEDELIVERY&filter=gainer&pageSize=30&pageNumber=1&sort=change&sortOrder=desc"
nse_losers_url = "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm?symbol=INDEX%20NIFTY&segmentLink=17&symbolCount=2&series=EQ&dataType=PRICEVOLUMEDELIVERY&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERY&dataType=PRICEVOLUMEDELIVERY&filter=loser&pageSize=30&pageNumber=1&sort=change&sortOrder=asc"

top_gainers = get_top_movers(nse_gainers_url)
top_losers = get_top_movers(nse_losers_url, gainers=False)

print("Top 20 Gainers:")
for gainer in top_gainers:
  print(f"\t- Symbol: {gainer['symbol']}, Change: {gainer['change']}, Percentage: {gainer['percentage']}")

print("\nTop 20 Losers:")
for loser in top_losers:
  print(f"\t- Symbol: {loser['symbol']}, Change: {loser['change']}, Percentage: {loser['percentage']}")

