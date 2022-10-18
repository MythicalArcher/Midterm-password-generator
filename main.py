from function import generator

length = int(input("What is the desired length of this password?\n> "))
options = int(input("What type of password do you prefer?\n1. Alpha-numerical\n2. Numerical\n3. Everything, symbols, number, letters, all that jazz\n"))
# exceptions= input("What character's do you NOT want in your password?")

generator(options, length)
