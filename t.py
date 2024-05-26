import pandas as pd
import yfinance as yf

def get_top_movers(exchange, gainers=True):
  """
  Fetches top gainers (or losers) data from Yahoo Finance for a specific exchange.

  Args:
      exchange (str): Name of the stock exchange (BSE or NSE).
      gainers (bool, optional): Whether to fetch data for gainers (True) or losers (False). Defaults to True.

  Returns:
      pd.DataFrame: DataFrame containing information about top movers, or None on error.
  """
  # Define index symbols for each exchange
  index_symbols = {
      "BSE": "^SENSEX",
      "NSE": "^NSEI"
  }

  # Validate exchange
  if exchange not in index_symbols:
    raise ValueError(f"Invalid exchange: {exchange}")

  # Download historical data (recent day) for the exchange index
  try:
    data = yf.download(index_symbols[exchange], period="1d", interval="1m")["Close"]
  except Exception as e:
    print(f"Error downloading data for {exchange}: {e}")
    return None

  # Calculate daily percentage change
  daily_change = (data - data.shift(1)) / data.shift(1) * 100

  # Get list of constituents for the exchange index
  # (Replace with logic to retrieve constituents from a reliable source)
  constituents_url = f"https://www1.nseindia.com/products/content/equities/equities/eq_security.htm?symbol={index_symbols[exchange]}&segmentLink=17&symbolCount=2&series=EQ&dataType=PRICEVOLUMEDELIVERY&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERY&dataType=PRICEVOLUMEDELIVERY&filter=companyinfo&pageSize=50&pageNumber=1&sort=change&sortOrder=desc"  # Example for NSE
  # TODO: Implement logic to fetch constituents from a reliable source based on the exchange

  # Filter data for index constituents (replace with fetched constituents)
  constituents = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFC.NS", "ITC.NS"]  # Placeholder

  filtered_data = daily_change[constituents]

  # Sort by daily change (descending for gainers, ascending for losers)
  sorted_data = filtered_data.sort_values(ascending=not gainers)[:20]

  # Create DataFrame with formatted data
  df = pd.DataFrame({
    "Symbol": sorted_data.index.to_list(),
    "Change": [f"{value:.2f}%" for value in sorted_data.values]
  })

  return df

def print_table(df, title):
  """
  Prints a formatted table from a pandas DataFrame.

  Args:
      df (pd.DataFrame): DataFrame to be printed.
      title (str): Title for the table.
  """
  print(f"\n{title}:")
  print(df.to_string(index=False))

if __name__ == "__main__":
  # Get top gainers and losers for BSE
  bse_gainers = get_top_movers("BSE")
  bse_losers = get_top_movers("BSE", gainers=False)

  # Get top gainers and losers for NSE
  nse_gainers = get_top_movers("NSE")
  nse_losers = get_top_movers("NSE", gainers=False)

  # Print tables
  print_table(bse_gainers, "Top 20 BSE Gainers")
  print_table(bse_losers, "Top 20 BSE Losers")
  print_table(nse_gainers, "Top 20 NSE Gainers")
  print_table(nse_losers, "Top 20 NSE Losers")

  # Disclaimer regarding exchange data retrieval
  print("\nDisclaimer: This script retrieves exchange index constituents from a placeholder list. Implement logic to fetch them from a reliable source for each exchange (e.g., NSE website scraping).")

