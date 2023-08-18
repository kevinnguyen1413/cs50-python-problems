def main():
    sentence = str(input('Input: '))
    remove_vowels(sentence)
    
def remove_vowels(sentence):
    no_vowels_sentence = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in sentence:
        if i.lower() in vowels:
            del i
        else:
            no_vowels_sentence += i
    return print(f'Output: {no_vowels_sentence}')

main()