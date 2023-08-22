def main():
    item_cost()

def item_cost():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        try:
            choice = input('Item: ').lower()
        except EOFError:
            break
        else:
            for k in menu:
                try:
                    if choice == k.lower():
                        total += menu[choice.title()]
                        print(f'${total:.2f}')
                except KeyError:
                    continue

main()