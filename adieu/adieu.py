import inflect

inf = inflect.engine()
name_list = []

def main():
    oxford_comma()

def oxford_comma():
    while True:
        try:
            name = input('Name: ')
            name_list.append(name)
        except EOFError:
            print(f'Adieu, adieu, to {inf.join(name_list)}')
            break
        else:
            continue
main()