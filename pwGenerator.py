import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

pass_length = int(input("password length [6-15]\n: "))

def passgen ():
    pwd = ""
    for x in range(pass_length):
        pwd += random.choice(chars)
    print(pwd)

while True:
    passgen()
    x = str(input(": "))
    if x == "0":
        break
    else:
        pass_length = int(input("password must be [6-15]\n: "))
        passgen()
        
