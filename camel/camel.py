def main():
    camel_case = input('camelCase: ')
    print(snake_case(camel_case))
    
def snake_case(camel_case):
    convert_case = ''
    for i in camel_case:
        if i.isupper():
            convert_case +='_' + i.lower()
        else:
            convert_case += i
    return convert_case

main()