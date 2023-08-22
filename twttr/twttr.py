def main():
    sentence = str(input('Input: '))
    remove_vowels(sentence)
    
def remove_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels_sentence = ''.join([char for char in sentence if char.lower() not in vowels])
    return print(f'Output: {no_vowels_sentence}')

main()