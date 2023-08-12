import sys

def main():
    print_cs50()
    
def print_cs50():
    if len(sys.argv) < 2:
        sys.exit('Too few arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many arguments')
    check50 = 'check50 cs50/problems/2022/python/'
    submit50 = 'submit50 cs50/problems/2022/python/'
    print(check50, sys.argv[1], sep='')
    print(submit50, sys.argv[1], sep='')
    return

main()