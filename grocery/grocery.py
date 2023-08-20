def main():
    grocery_list()

def grocery_list():
    to_buy_dict = {}
    while True:
        try:
            item = input('').lower()
            if item in to_buy_dict:
                to_buy_dict[item] += 1
            else:
                to_buy_dict[item] = 1
        except EOFError:
            for item in sorted(to_buy_dict):
                print(to_buy_dict[item], item.upper())
            break

main()