import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid number of bitcoins.")
        sys.exit(1)
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        bitcoin_data = response.json()
        bitcoin_price_usd = bitcoin_data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error: Failed to fetch Bitcoin price ({e})")
        sys.exit(1)
    except KeyError:
        print("Error: Unexpected response from API")
        sys.exit(1)
    cost_usd = bitcoins * bitcoin_price_usd
    print(f"Cost of {bitcoins:.4f} Bitcoins: ${cost_usd:,.4f}")

if __name__ == "__main__":
    main()
