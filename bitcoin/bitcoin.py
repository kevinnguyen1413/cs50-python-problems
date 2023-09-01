import requests
import sys

if len (sys.argv) != 2:
    sys.exit('Missing command-line argument')

try:
    btc_amount = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')


def main():
    bitcoin_price()

def bitcoin_price():
    try:
        chart = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        chart_json = chart.json()
        converted_btc = chart_json["bpi"]["USD"]["rate_float"]*btc_amount
        print(f'${converted_btc:,.4f}')     
    except requests.RequestException:
        print('Check code for error(s)')
        
main()