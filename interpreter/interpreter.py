def main():
    interpreter('algebra')

def interpreter(expression):
    expression = input('Expression: ').strip().split()
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])
    
    if y == '+':
        output = x+z
    elif y == '-':
        output = x-z
    elif y == '*':
        output = x*z
    elif y == '/' and z != 0:
        output = x/z
    else:
        return print('Calculator needs further development. Apologies :(')
    return print(float(output))

main()