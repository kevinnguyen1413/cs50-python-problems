def main():
    print_cs50('Retry')
    
def print_cs50(problem):
    problem = input('What is the name of the problem?\n')
    check50 = 'check50 cs50/problems/2022/python/'
    submit50 = 'submit50 cs50/problems/2022/python/'
    print(check50 + problem.strip().lower())
    print(submit50 + problem.strip().lower())
    return

main()
    
    