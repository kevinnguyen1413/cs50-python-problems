from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
font_list = figlet.getFonts()

def main():
    figleter()

def figleter():
    if len(sys.argv) == 1:
        text = input('Input: ')
        figlet.setFont(font=random.choice(font_list))
        print(f'Output: {figlet.renderText(text)}')
    elif (len(sys.argv) > 0) and (sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in font_list):
        sys.exit('Invalid usage')
    else:
        text = input('Input: ')
        figlet.setFont(font=sys.argv[2])
        print(f'Output: {figlet.renderText(text)}')
    
main()