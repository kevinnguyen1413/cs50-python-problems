def main():
    greet('Kevin')
    
def greet(sentence):
    sentence = input('Greeting: ').lower().strip()
    if 'hello' in sentence:
        return print('$0')
    elif list(sentence)[0] == 'h':
        return print('$20')
    else:
        return print('$100')
    return

main()