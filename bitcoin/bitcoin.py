import requests
import sys

if len (sys.argv) != 2:
    print('Missing command-line argument')
    sys.exit()
try:
    btc_amount = float(sys.argv[1])
except ValueError:
    print('Command-line argument is not a number')


def main():
    bitcoin_price()

def bitcoin_price():
    try:
        print('Hello')
    except requests.RequestException:
        print('hello')
        
main()