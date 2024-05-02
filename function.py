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
        
def gen_emo():
    emo = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923","\U0001f642","\U0001F607"]
    return random.choice(emo)

        
