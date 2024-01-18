# config.py

import configparser

# Read config from INI
config = configparser.ConfigParser()
config.read('config.ini')

# Get values from the INI file
REFRESH_INTERVAL = config['Settings'].get('refresh_interval') or 10
