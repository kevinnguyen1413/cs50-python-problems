def main():
    insert_coin('5')

def insert_coin(coin):
    amount_due = 50
    accepted_coins = [5, 10, 25]
    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        coin = int(input('Insert Coin, only in 5, 10, or 25 cents : '))
        if coin not in accepted_coins:
            print('Please insert only 5, 10, or 25 cents')
            continue
        amount_due -= coin
        if amount_due <= 0:
            print(f'Change Owed: {abs(amount_due)}')
            break
    return

main()