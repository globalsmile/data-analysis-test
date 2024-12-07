import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Define exchanges and their P2P links
exchanges = [
    {"name": "Binance", "link": "https://p2p.binance.com/en"},
    {"name": "OKX", "link": "https://www.okx.com/ru/p2p-markets/kzt/buy-usdt"},
    {"name": "KuCoin", "link": "https://www.kucoin.com/ru/otc/buy/USDT-USD"},
    {"name": "HTX", "link": "https://www.htx.com/en-us/fiat-crypto/trade/buy-usdt-rub/"},
    {"name": "Bybit", "link": "https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=UAH&paymentMethod="},
    {"name": "Gate", "link": "https://www.gate.io/ru/c2c/market?fiat=UAH"},
    {"name": "Poloniex", "link": "https://poloniex.com/p2p/markets/buy/usdt-kzt"},
    {"name": "Qmall", "link": "https://qmall.io/ru/p2p/?crypto=USDT&fiat=UAH"},
    {"name": "HODLHODL", "link": "https://hodlhodl.com/offers/buy?filters%5Bcurrency_code%5D=UAH&pagination%5Boffset%5D=0"},
    {"name": "LocalCoinSwap", "link": "https://localcoinswap.com/ru/buy/crypto/ukraine"},
    {"name": "Paxful", "link": "https://paxful.com/ru/buy-tether/with-any-payment-method/UAH?currencyCode=UAH&currencyId=200&paymentMethod=with-any-payment-method&countryIso=WORLDWIDE&usersCountryIso=WORLDWIDE&isUsersCountryIsoEnabled=true&hasScroll=true"},
    {"name": "BitValve", "link": "https://www.bitvalve.com/buy"},
    {"name": "Bitfinex", "link": "https://p2p.bitfinex.com/trade/sell/BTC/"},
    {"name": "BitPapa", "link": "https://bitpapa.com/dashboard"},
    {"name": "NoOnes", "link": "https://noones.com/ru"},
    {"name": "Koshelek.ru", "link": "https://koshelek.ru/authorization/login"},
    {"name": "Bitget", "link": "https://www.bitget.com/uk/"},
    {"name": "MEXC", "link": "https://otc.mexc.com/ru-RU"},
    {"name": "Remitano", "link": "https://remitano.com/us/p2p/usdt"},
    {"name": "BingX", "link": "https://bingx.paycat.com/en/trade/self-selection?fiat=RUB&type=1"},
    {"name": "CoinEx", "link": "https://www.coinex.com/en/p2p"},
    {"name": "Cryptomus", "link": "https://p2p.cryptomus.com/buy-usdt?page=1&fiatCurrency=EUR"}
]

# Initialize WebDriver
driver = webdriver.Chrome()

# Define the output file
output_file = "p2p_data_complete.csv"

# Open CSV file for writing
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow([
        "Exchange's Name", "Country", "Currency", "Vendor's Name",
        "Amount of Deals", "Bank's Name", "Owner's Name", "CC Number",
        "Account Number", "IBAN", "BIC / SWIFT", "E-mail / Contact"
    ])
    
    # Iterate through exchanges
    for exchange in exchanges:
        print(f"Scraping data from {exchange['name']}...")
        driver.get(exchange["link"])
        time.sleep(5)  # Allow page to load
        
        # Example logic to scrape data
        try:
            rows = driver.find_elements(By.CSS_SELECTOR, ".vendor-row")  # Adjust based on HTML structure
            for row in rows:
                vendor_data = [
                    exchange["name"],  # Exchange's Name
                    "N/A",  # Country (placeholder; detect dynamically if possible)
                    row.find_element(By.CSS_SELECTOR, ".currency").text if row.find_elements(By.CSS_SELECTOR, ".currency") else "N/A",  # Currency
                    row.find_element(By.CSS_SELECTOR, ".vendor-name").text if row.find_elements(By.CSS_SELECTOR, ".vendor-name") else "N/A",  # Vendor's Name
                    row.find_element(By.CSS_SELECTOR, ".deals").text if row.find_elements(By.CSS_SELECTOR, ".deals") else "N/A",  # Amount of Deals
                    row.find_element(By.CSS_SELECTOR, ".bank-name").text if row.find_elements(By.CSS_SELECTOR, ".bank-name") else "N/A",  # Bank's Name
                    row.find_element(By.CSS_SELECTOR, ".owner-name").text if row.find_elements(By.CSS_SELECTOR, ".owner-name") else "N/A",  # Owner's Name
                    "N/A",  # CC Number (not typically public; placeholder)
                    "N/A",  # Account Number (not typically public; placeholder)
                    "N/A",  # IBAN (placeholder)
                    "N/A",  # BIC / SWIFT (placeholder)
                    "N/A"   # E-mail / Contact (placeholder)
                ]
                writer.writerow(vendor_data)
        except Exception as e:
            print(f"Error scraping {exchange['name']}: {e}")

# Close WebDriver
driver.quit()

print(f"Data collection completed. Saved to {output_file}.")

