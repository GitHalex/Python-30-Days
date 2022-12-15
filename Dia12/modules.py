""" import os

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print(f'Welcome: {sys.argv[1]} enjoy challenge {sys.argv[2]}') """


""" # to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version """

""" from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(round(mean(ages), 2))
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages)) """

""" from math import pi
print(pi) """


""" from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(log10(100))    # 2 """


""" from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
 """

""" import random
import string

def random_alnum(size=6):
   # Generate random 6 character alphanumeric string
   chars = string.ascii_letters + string.digits
   code = ''.join(random.choice(chars) for _ in range(size))

   return code

print(random_alnum()) """

""" def user_id_gen_by_user(num_character, num_id):
   aux = 0
   while aux < num_id:
      chars = string.ascii_letters+string.digits
      code = ''.join(random.choice(chars) for _ in range(num_character))
      print(code)
      aux += 1

num_character = int(input('Ingrese el numero de caracteres: '))
num_id = int(input('Cantidad de ids generados: '))

print(user_id_gen_by_user(num_character, num_id)) """

""" from random import randint

def rgb_color_gen():
   primer = randint(0,255)
   segundo = randint(0,255)
   tercero = randint(0,255)

   return f'rgb({primer},{segundo},{tercero})'

print(rgb_color_gen()) """




