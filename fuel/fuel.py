def main():
    fraction_convert()
    
def fraction_convert():
    while True:
        try:
            frac = input('Fraction: ').split('/')
            num = int(frac[0])
            denom = int(frac[1])
            percentage = round(num/denom*100)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        if num > denom:
            continue
        else:
            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(f'{percentage}%')
        return
                
main()