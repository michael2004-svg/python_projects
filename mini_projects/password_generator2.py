import random
import string

def pwg_gen(min_leght):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    character=letters
    character +=digits
    character += special
    #meets_criteria=letters and digits and special
    pwd=''
    while  len(pwd)<min_leght:
        newchar=random.choice(character)
        pwd +=newchar
    return pwd
min_length=int(input("enter the min length for your password  "))
password = pwg_gen(min_length)  
print('generated password is:', password)