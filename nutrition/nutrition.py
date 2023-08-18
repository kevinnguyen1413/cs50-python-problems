fruits_cal = {'Apple': '130', 'Avocado California':'50', 'Banana':'110', 'Cantaloupe':'50', 'Grapefruit':'60', 'Grapes':'90', 'Honeydew Melon':'50', 'Kiwifruit':'90',\
    'Lemon': '15', 'Lime': '20', 'Orange': '80', 'Nectarine': '60', 'Peach': '60', 'Pear': '100', 'Pineapple': '50', 'Plums': '70',\
    'Strawberries': '50', 'Sweet Cherries': '100', 'Tangerine': '50', 'Watermelon': '80'}

def main():
    fruit = input('Item: ').lower()
    check_calories(fruit)
    
def check_calories(s):
    for k, v in fruits_cal.items():
        if s == k.lower():
            print('Calories:', v)
        else:
            print('Please enter a fruit in FDA raw fruits list')
            break

main()