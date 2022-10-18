from classes import ascii
# Random is a psudo-random method (I believe is the right term), since I wanted it be truly random rather than predictable I opted to using the secrets method.
# https://docs.python.org/3/library/secrets.html#secrets.choice
import secrets

# def generator(options, length, exceptions):



def generator(options, length):
    if options == 1:
        # char = ascii.all() + ascii.num()
        # print(char) testing
        # https://www.w3schools.com/python/ref_string_join.asp
        
        print("".join(secrets.choice(ascii.all() + ascii.num()) for i in range(length)))
    
    elif options == 2:
        print("".join(secrets.choice(ascii.num()) for i in range(length)))
    
    elif options == 3:
        print("".join(secrets.choice(ascii.all() + ascii.num() + ascii.symbol()) for i in range(length)))

