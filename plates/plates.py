import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


"""“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”"""

def is_valid(s):
    if s[0].isalpha() and s[1].isalpha():
        return True

    
    if len(s) in range(2, 7):
        return True
    elif len(s) not in range(2,7):
        return False
    
    for i in s:
        if i == string.punctuation:
            return False
        else:
            return True
    if s[2] != '0':
        return True
    
    if s[2:5].isnumeric() and s[6].isalpha():
        return False
    elif s[2:4].isnumeric() and s[5:6].isalpha():
        return False
    elif s[2:3].isnumeric() and s[4:6].isalpha():
        return False
    else:
        return True

main()