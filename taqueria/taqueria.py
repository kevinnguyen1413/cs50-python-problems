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
            if choice.title() not in menu:
                continue
        except EOFError:
            break
        else:
            total += sum([menu[k] for k in menu if choice == k.lower()])
            print(f'${total:.2f}')

main()