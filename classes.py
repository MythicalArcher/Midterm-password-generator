import string 

# To keep me sane I've decided to place all of the string methods into classes to make it easier to read/type.
class ascii():
    def all():
        return string.ascii_letters
    # def upperCase():
    #     return string.ascii_uppercase
    # def lowerCase():
    #     return string.ascii_lowercase
    def num():
        return string.digits
    def symbol():
        return string.punctuation

