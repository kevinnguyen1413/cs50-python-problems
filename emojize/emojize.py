import emoji as em

def main():
    emote = input('Input: ')
    emojizer(emote)
    
def emojizer(s):
    print(em.emojize(s))

main()