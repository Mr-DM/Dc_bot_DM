import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

 
def coin_toss():
    coin = random.randint(0, 2)
    if coin == 0:
        return "True"
    else:
        return "False"  
        

        
