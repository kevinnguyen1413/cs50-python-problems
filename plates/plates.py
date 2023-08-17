import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (start_alpha(s) and plate_length(s) and num_after_alpha(s) and first_non_zero(s) and no_punctuations(s)) == True:
        return True
    return False

def start_alpha(s):
    if s[0:2].isalpha():
        return True
    return False

def plate_length(s):
    if len(s) in range(2, 7):
        return True
    return False

def no_punctuations(s):
    x = list(string.punctuation)
    for i in s:
        if i in x:
            return False
    return True

def first_non_zero(s):
    if s[2] != '0':
        return True
    return False

def num_after_alpha(s):
    if s[-1].isalpha() and any(s[i].isnumeric() for i in range(2, len(s))):
        return False
    for i in range(2, len(s)):
        if s[i].isnumeric() and s[i-1].isalpha() and s[i+1].isalpha():
            return False
    return True
    
main()