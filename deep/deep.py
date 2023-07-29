def main():
    the_answer(None)
        
def the_answer(everything):
    answer = input('What is the answer to the Great Question of Life, the Universe and Everything? ')
    everything = answer.strip().lower()
    if everything == '42' or everything == 'forty-two' or everything == 'forty two':
        print('Yes')
    else:
        print('No')
    return

main()